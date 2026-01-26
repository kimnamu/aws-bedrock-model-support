/**
 * AWS Bedrock Model Availability - Main Application
 */

const DATA_URL = 'data/availability.json';

let allData = null;
let allRegions = [];
let allProviders = [];

/**
 * Initialize the application
 */
async function init() {
    try {
        const response = await fetch(DATA_URL);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        allData = await response.json();

        // Extract regions and providers
        allRegions = Object.keys(allData.regions || {}).sort();
        allProviders = Object.keys(allData.providers || {}).sort();

        // Update stats
        updateStats();

        // Populate filters
        populateFilters();

        // Render provider sections
        renderProviderSections();

        // Hide loading, show content
        document.getElementById('loading').classList.add('d-none');

        // Update last updated timestamp
        if (allData.generated_at) {
            document.getElementById('last-updated').textContent = `Last updated: ${allData.generated_at}`;
        }
    } catch (error) {
        console.error('Failed to load data:', error);
        document.getElementById('loading').classList.add('d-none');
        document.getElementById('error').classList.remove('d-none');
    }
}

/**
 * Update statistics cards
 */
function updateStats() {
    // Count total unique models
    let totalModels = 0;
    const uniqueModels = new Set();

    for (const provider of Object.keys(allData.providers || {})) {
        const models = allData.providers[provider];
        for (const modelId of Object.keys(models)) {
            uniqueModels.add(modelId);
        }
    }

    document.getElementById('total-models').textContent = uniqueModels.size;
    document.getElementById('total-regions').textContent = allRegions.length;
    document.getElementById('total-providers').textContent = allProviders.length;
}

/**
 * Populate filter dropdowns
 */
function populateFilters() {
    const providerFilter = document.getElementById('provider-filter');
    const regionFilter = document.getElementById('region-filter');

    // Add provider options
    allProviders.forEach(provider => {
        const option = document.createElement('option');
        option.value = provider;
        option.textContent = provider;
        providerFilter.appendChild(option);
    });

    // Add region options
    allRegions.forEach(region => {
        const option = document.createElement('option');
        option.value = region;
        option.textContent = region;
        regionFilter.appendChild(option);
    });

    // Add event listeners
    providerFilter.addEventListener('change', filterSections);
    regionFilter.addEventListener('change', filterSections);
    document.getElementById('search-input').addEventListener('input', filterSections);
}

/**
 * Render all provider sections
 */
function renderProviderSections() {
    const container = document.getElementById('provider-sections');
    container.innerHTML = '';

    allProviders.forEach(provider => {
        const section = createProviderSection(provider);
        container.appendChild(section);
    });
}

/**
 * Create a provider section element
 */
function createProviderSection(provider) {
    const models = allData.providers[provider] || {};
    const modelIds = Object.keys(models);

    // Get regions that have at least one model from this provider
    const providerRegions = new Set();
    modelIds.forEach(modelId => {
        const regions = models[modelId].regions || [];
        regions.forEach(r => providerRegions.add(r));
    });
    const sortedRegions = Array.from(providerRegions).sort();

    // Create section element
    const section = document.createElement('div');
    section.className = 'provider-section';
    section.dataset.provider = provider;

    // Header
    const header = document.createElement('div');
    header.className = 'provider-header';
    header.innerHTML = `
        <h3>${provider}</h3>
        <div>
            <span class="badge bg-light text-dark me-2">${modelIds.length} models</span>
            <span class="badge bg-light text-dark me-2">${sortedRegions.length} regions</span>
            <span class="toggle-icon">&#9660;</span>
        </div>
    `;
    header.addEventListener('click', () => toggleSection(section));
    section.appendChild(header);

    // Content
    const content = document.createElement('div');
    content.className = 'provider-content';

    if (modelIds.length === 0 || sortedRegions.length === 0) {
        content.innerHTML = '<p class="text-muted">No models available</p>';
    } else {
        const table = createAvailabilityTable(provider, modelIds, sortedRegions, models);
        content.appendChild(table);
    }

    section.appendChild(content);
    return section;
}

/**
 * Create availability table for a provider
 */
function createAvailabilityTable(provider, modelIds, regions, models) {
    const tableWrapper = document.createElement('div');
    tableWrapper.className = 'table-responsive';

    const table = document.createElement('table');
    table.className = 'table table-sm availability-table';
    table.id = `table-${provider.replace(/\s+/g, '-').toLowerCase()}`;

    // Header
    const thead = document.createElement('thead');
    let headerRow = '<tr><th>Model</th>';
    regions.forEach(region => {
        headerRow += `<th class="region-header">${region}</th>`;
    });
    headerRow += '</tr>';
    thead.innerHTML = headerRow;
    table.appendChild(thead);

    // Body
    const tbody = document.createElement('tbody');

    // Sort models by display name
    const sortedModels = modelIds.sort((a, b) => {
        const nameA = getDisplayName(a);
        const nameB = getDisplayName(b);
        return nameA.localeCompare(nameB);
    });

    sortedModels.forEach(modelId => {
        const modelRegions = new Set(models[modelId].regions || []);
        const displayName = getDisplayName(modelId);

        let row = `<tr data-model="${modelId}"><td class="model-name" title="${modelId}">${displayName}</td>`;
        regions.forEach(region => {
            if (modelRegions.has(region)) {
                row += '<td><span class="check-icon">&#10003;</span></td>';
            } else {
                row += '<td><span class="cross-icon">&#8212;</span></td>';
            }
        });
        row += '</tr>';
        tbody.innerHTML += row;
    });

    table.appendChild(tbody);
    tableWrapper.appendChild(table);

    return tableWrapper;
}

/**
 * Toggle provider section collapse/expand
 */
function toggleSection(section) {
    const content = section.querySelector('.provider-content');
    const icon = section.querySelector('.toggle-icon');

    content.classList.toggle('collapsed');
    icon.classList.toggle('collapsed');
}

/**
 * Filter sections based on selected filters and search
 */
function filterSections() {
    const providerFilter = document.getElementById('provider-filter').value;
    const regionFilter = document.getElementById('region-filter').value;
    const searchTerm = document.getElementById('search-input').value.toLowerCase();

    const sections = document.querySelectorAll('.provider-section');

    sections.forEach(section => {
        const provider = section.dataset.provider;
        const rows = section.querySelectorAll('tbody tr');

        // Check provider filter
        if (providerFilter && provider !== providerFilter) {
            section.style.display = 'none';
            return;
        }

        let hasVisibleRows = false;

        rows.forEach(row => {
            const modelId = row.dataset.model;
            const displayName = getDisplayName(modelId).toLowerCase();
            const modelRegions = allData.providers[provider]?.[modelId]?.regions || [];

            // Check region filter
            const passesRegionFilter = !regionFilter || modelRegions.includes(regionFilter);

            // Check search filter
            const passesSearchFilter = !searchTerm ||
                displayName.includes(searchTerm) ||
                modelId.toLowerCase().includes(searchTerm);

            if (passesRegionFilter && passesSearchFilter) {
                row.style.display = '';
                hasVisibleRows = true;
            } else {
                row.style.display = 'none';
            }
        });

        // Show/hide section based on whether it has visible rows
        if (!providerFilter) {
            section.style.display = hasVisibleRows ? '' : 'none';
        } else {
            section.style.display = '';
        }
    });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', init);
