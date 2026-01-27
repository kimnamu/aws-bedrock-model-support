"""README Updater - Updates the availability section in README.md"""

import logging
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from src.models import REGION_NAMES, AvailabilityMatrix, ProviderSummary, get_display_name

logger = logging.getLogger(__name__)

# Timezone definitions
TZ_UTC = timezone.utc
TZ_PST = timezone(timedelta(hours=-8))  # US Pacific Standard Time
TZ_KST = timezone(timedelta(hours=9))   # Korea Standard Time


class ReadmeUpdateError(Exception):
    """Exception raised when README update fails"""

    pass


class ReadmeUpdater:
    """Class to update the availability section in README.md"""

    SECTION_START = "<!-- BEDROCK_AVAILABILITY_START -->"
    SECTION_END = "<!-- BEDROCK_AVAILABILITY_END -->"

    DEFAULT_TEMPLATE = """# AWS Bedrock Model Availability Tracker

Track AWS Bedrock model availability across regions.

## Model Availability

{section_start}
{section_end}

## Usage

This repository is automatically updated every hour.

## License

MIT License
"""

    def __init__(self) -> None:
        self.section_start = self.SECTION_START
        self.section_end = self.SECTION_END

    def _generate_provider_anchor(self, provider: str) -> str:
        """Convert provider name to anchor ID."""
        return provider.lower().replace(" ", "-").replace(".", "")

    def _format_timestamps(self, utc_time: datetime) -> str:
        """Format timestamp in multiple timezones as a clean table."""
        utc_str = utc_time.strftime("%Y-%m-%d %H:%M")
        pst_time = utc_time.astimezone(TZ_PST)
        pst_str = pst_time.strftime("%Y-%m-%d %H:%M")
        kst_time = utc_time.astimezone(TZ_KST)
        kst_str = kst_time.strftime("%Y-%m-%d %H:%M")

        return f"| UTC | PST (US West) | KST (Korea) |\n|:---:|:---:|:---:|\n| {utc_str} | {pst_str} | {kst_str} |"

    def generate_markdown_table(
        self,
        matrix: AvailabilityMatrix,
        provider_region_counts: Dict[str, Dict[str, int]],
        model_region_availability: Optional[Dict[str, Dict[str, set]]] = None,
    ) -> str:
        """
        Generate markdown table for model availability.

        Args:
            matrix: Availability matrix
            provider_region_counts: Model count per provider per region
            model_region_availability: Region availability per model per provider

        Returns:
            str: Markdown formatted table
        """
        providers = sorted(provider_region_counts.keys())

        if not providers:
            return self._generate_empty_table(matrix.generated_at)

        regions = [r for r in matrix.regions if r.error is None]

        if not regions:
            return self._generate_empty_table(matrix.generated_at)

        lines: List[str] = []

        # Badges
        lines.append(f"![Last Updated](https://img.shields.io/badge/Last%20Updated-{matrix.generated_at.strftime('%Y--%-m--%-d')}-blue)")
        lines.append(f" ![Regions](https://img.shields.io/badge/Regions-{len(regions)}-green)")
        lines.append(f" ![Providers](https://img.shields.io/badge/Providers-{len(providers)}-orange)")
        lines.append("")

        # Timestamp table
        lines.append("### Last Updated")
        lines.append("")
        timestamp = self._format_timestamps(matrix.generated_at)
        lines.append(timestamp)
        lines.append("")

        # Table of Contents as a table
        lines.append("## Table of Contents")
        lines.append("")
        lines.append("| Provider | Models | Regions |")
        lines.append("|:---------|-------:|--------:|")

        for provider in providers:
            anchor = self._generate_provider_anchor(provider)
            if model_region_availability and provider in model_region_availability:
                model_count = len(model_region_availability[provider])
            else:
                model_count = sum(provider_region_counts.get(provider, {}).values())
            region_count = len([r for r in regions if provider_region_counts.get(provider, {}).get(r.region, 0) > 0])
            lines.append(f"| [{provider}](#{anchor}) | {model_count} | {region_count} |")

        lines.append("")
        lines.append("---")
        lines.append("")

        # Provider model-region matrix
        for provider in providers:
            anchor = self._generate_provider_anchor(provider)
            available_regions = [r for r in regions if provider_region_counts.get(provider, {}).get(r.region, 0) > 0]

            if model_region_availability and provider in model_region_availability:
                models = model_region_availability[provider]
                model_count = len(models)

                # Collapsible section
                lines.append(f"<details>")
                lines.append(f"<summary><h3 id=\"{anchor}\">{provider} ({model_count} models, {len(available_regions)} regions)</h3></summary>")
                lines.append("")

                if available_regions and models:
                    # Table header
                    header = "| Model |"
                    for r in available_regions:
                        header += f" {r.region} |"
                    lines.append(header)

                    # Separator
                    separator = "|:------|"
                    for _ in available_regions:
                        separator += ":---:|"
                    lines.append(separator)

                    # Model rows (sorted by display name)
                    sorted_models = sorted(
                        models.items(),
                        key=lambda x: get_display_name(x[0])
                    )
                    for model_id, model_data in sorted_models:
                        if isinstance(model_data, dict):
                            model_regions = model_data.get("regions", set())
                        else:
                            model_regions = model_data

                        display_name = get_display_name(model_id)
                        row = f"| {display_name} |"
                        for r in available_regions:
                            if r.region in model_regions:
                                row += " ✅ |"
                            else:
                                row += " ❌ |"
                        lines.append(row)

                    lines.append("")
                else:
                    lines.append("*No models available*")
                    lines.append("")

                lines.append("</details>")
                lines.append("")
            else:
                # Fallback: legacy format
                lines.append(f"### <a id=\"{anchor}\"></a>{provider}")
                lines.append("")
                lines.append(f"**{len(available_regions)} regions** with models")
                lines.append("")
                if available_regions:
                    lines.append("| Region | Models |")
                    lines.append("|--------|--------|")
                    for region in available_regions:
                        count = provider_region_counts.get(provider, {}).get(region.region, 0)
                        if count > 0:
                            lines.append(f"| {region.region} | {count} |")
                    lines.append("")

        # Failed regions
        error_regions = [r for r in matrix.regions if r.error is not None]
        if error_regions:
            lines.append("---")
            lines.append("")
            lines.append("### Failed Regions")
            lines.append("")
            for region in error_regions:
                lines.append(f"- **{region.region}**: {region.error}")
            lines.append("")

        return "\n".join(lines)

    def _generate_empty_table(self, generated_at: datetime) -> str:
        """Generate empty table when no data is available."""
        timestamp = self._format_timestamps(generated_at)
        return f"No model data available.\n\n### Last Updated\n\n{timestamp}"

    def generate_summary_section(self, summary: ProviderSummary) -> str:
        """
        Generate summary section by provider.

        Args:
            summary: Provider summary data

        Returns:
            str: Markdown formatted summary section
        """
        lines: List[str] = []
        lines.append("## Summary")
        lines.append("")
        lines.append("| Metric | Value |")
        lines.append("|--------|-------|")
        lines.append(f"| Total Models | **{summary.total_models}** |")
        lines.append(f"| Total Regions | **{summary.total_regions}** |")
        lines.append(f"| Providers | **{len(summary.providers)}** |")
        lines.append("")
        lines.append("### Provider Breakdown")
        lines.append("")
        lines.append("| Provider | Models | Regions |")
        lines.append("|----------|--------|---------|")

        for provider in sorted(summary.providers, key=lambda p: p.provider_name):
            model_count = len(provider.models)
            region_count = len(provider.region_availability)
            lines.append(f"| {provider.provider_name} | {model_count} | {region_count} |")

        return "\n".join(lines)

    def update_readme(
        self,
        readme_path: str,
        table_content: str,
        summary_content: Optional[str] = None,
    ) -> None:
        """
        Update the availability section in README.md file.

        Property 5: README section preservation
        Content outside the availability markers (BEDROCK_AVAILABILITY_START/END) must not be modified.

        Args:
            readme_path: Path to README.md file
            table_content: New table content
            summary_content: Summary content (optional)
        """
        path = Path(readme_path)

        # Create new content (table first, Summary at the bottom)
        full_content = table_content
        if summary_content:
            full_content = f"{table_content}\n\n---\n\n{summary_content}"

        new_section = f"{self.section_start}\n\n{full_content}\n\n{self.section_end}"

        if path.exists():
            current_content = path.read_text(encoding="utf-8")

            # Find existing section
            pattern = re.compile(
                rf"{re.escape(self.section_start)}.*?{re.escape(self.section_end)}",
                re.DOTALL,
            )

            if pattern.search(current_content):
                # Replace existing section
                new_content = pattern.sub(new_section, current_content)
                logger.info(f"Updated existing section in {readme_path}")
            else:
                # If section not found, append to end of file
                new_content = current_content.rstrip() + "\n\n" + new_section + "\n"
                logger.warning(f"Section markers not found, appending to {readme_path}")
        else:
            # If file doesn't exist, create new from template
            new_content = self.DEFAULT_TEMPLATE.format(
                section_start=self.section_start,
                section_end=self.section_end,
            )
            new_content = new_content.replace(
                f"{self.section_start}\n{self.section_end}",
                new_section,
            )
            logger.info(f"Created new README file at {readme_path}")

        path.write_text(new_content, encoding="utf-8")

    def create_default_readme(self, readme_path: str) -> None:
        """
        Create a README.md file with default template.

        Args:
            readme_path: Path to README.md file
        """
        path = Path(readme_path)

        if path.exists():
            logger.warning(f"README file already exists at {readme_path}")
            return

        content = self.DEFAULT_TEMPLATE.format(
            section_start=self.section_start,
            section_end=self.section_end,
        )

        path.write_text(content, encoding="utf-8")
        logger.info(f"Created default README at {readme_path}")

    def get_section_content(self, readme_path: str) -> Optional[str]:
        """
        Extract the availability section content from README file.

        Args:
            readme_path: Path to README.md file

        Returns:
            Section content or None
        """
        path = Path(readme_path)

        if not path.exists():
            return None

        content = path.read_text(encoding="utf-8")

        pattern = re.compile(
            rf"{re.escape(self.section_start)}(.*?){re.escape(self.section_end)}",
            re.DOTALL,
        )

        match = pattern.search(content)
        if match:
            return match.group(1).strip()

        return None
