/* Bedrock Model Explorer. Plain JS, no build step.
   Data: data/catalog.json (Bedrock control-plane snapshot), data/history.json (region changes
   replayed from the hourly tracker commits), data/notes.json (measured behaviour), and the
   hourly availability.json straight from GitHub so a brand-new model shows up before the
   catalog is rebuilt. */
const LIVE = 'https://raw.githubusercontent.com/kimnamu/aws-bedrock-model-support/main/docs/data/availability.json';
const $ = s => document.querySelector(s);
const esc = s => String(s ?? '').replace(/[&<>"]/g, c => ({'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[c]));
const DAY = 864e5, NOW = Date.now();
let C, H, P = null, N = {}, S = {region: 'us-east-1', tab: 'models', chips: new Set()};

const CHIPS = [
  ['mine', 'In my region', m => avail(m, S.region) !== 'no'],
  ['vision', 'Image input', m => m.input.includes('IMAGE')],
  ['pdf', 'Documents', m => m.documents.length > 0],
  ['caching', 'Prompt caching', m => m.prompt_caching],
  ['reasoning', 'Reasoning effort', m => !!m.reasoning_field],
  ['openai', 'OpenAI-compatible API', m => m.openai_chat || m.openai_responses],
  ['batch', 'Batch', m => m.batch],
  ['long', '64k+ output', m => (m.max_tokens || 0) >= 65536],
  ['new', 'Released in 90 days', m => m.released && NOW - Date.parse(m.released) < 90 * DAY],
  ['legacy', 'Legacy', m => m.status === 'LEGACY'],
];

const fmtDate = s => s ? new Date(s).toISOString().slice(0, 10) : '—';
const daysTo = s => s ? Math.ceil((Date.parse(s) - NOW) / DAY) : null;
const k = n => n == null ? '—' : n >= 1000 ? Math.round(n / 1000) + 'k' : String(n);

/* ---------- how can this model be called from region r? ---------- */
function callIds(m, r) {
  const out = [];
  if ((m.regions[r] || []).includes('ON_DEMAND')) out.push({id: m.id, kind: 'bare', to: [r]});
  for (const pid of m.profiles || []) {
    const p = C.profiles[pid];
    if (p && p.from.includes(r)) out.push({id: pid, kind: p.scope === 'global' ? 'global' : 'geo', scope: p.scope, to: p.to});
  }
  const rank = {bare: 0, geo: 1, global: 2};
  return out.sort((a, b) => rank[a.kind] - rank[b.kind]);
}
function avail(m, r) {
  const ids = callIds(m, r);
  return !ids.length ? 'no' : ids[0].kind === 'bare' ? 'od' : 'ip';
}
const callableFrom = m => C.regions.filter(r => callIds(m, r).length);
const pill = a => a === 'od' ? '<span class="pill od">On-demand</span>' : a === 'ip' ? '<span class="pill ip">Profile only</span>' : '<span class="pill">Not offered</span>';
const kindNote = x => x.kind === 'bare' ? 'Runs in this region only.'
  : x.kind === 'global' ? `Global profile: routes across ${x.to.length} regions worldwide. Most capacity, data may leave your geography.`
  : `${x.scope.toUpperCase()} profile: stays inside ${x.to.join(', ')}.`;

/* ---------- facts derived from the API (no guessing) ---------- */
function gotchas(m) {
  const g = [];
  if (!C.regions.some(r => (m.regions[r] || []).includes('ON_DEMAND')))
    g.push(['warn', `The bare ID <code>${esc(m.id)}</code> has no on-demand throughput in any tracked region. Call an inference profile ID instead.`]);
  if (m.no_sampling) g.push(['warn', 'Bedrock marks sampling parameters as hidden for this model (temperature / top_p). Leave them unset unless the measured notes say otherwise.']);
  if (m.reasoning_field) g.push(['info', `Reasoning effort (API schema field <code>${esc(m.reasoning_field)}</code>): ${m.reasoning_levels.map(esc).join(', ')}.`]);
  if (m.max_tokens) g.push(['info', `Max output ${m.max_tokens.toLocaleString()} tokens${m.default_max_tokens ? `, default ${m.default_max_tokens.toLocaleString()}` : ''}.`]);
  if (m.system_role === false) g.push(['warn', 'No system role in Converse.']);
  if (m.status === 'LEGACY') g.push(['warn', `Legacy. ${m.eol ? `End of life ${fmtDate(m.eol)} (${daysTo(m.eol)} days).` : ''}`]);
  return g;
}

function snippet(m, id, r) {
  return `import boto3

client = boto3.client("bedrock-runtime", region_name="${r}")
resp = client.converse(
    modelId="${id}",
    messages=[{"role": "user", "content": [{"text": "Hello"}]}],
    inferenceConfig={"maxTokens": 1024},
)
print(resp["output"]["message"]["content"][0]["text"])`;
}

/* ---------- views ---------- */
function tiles() {
  const ms = Object.values(C.models), act = ms.filter(m => m.status !== 'LEGACY' && (m.pending || callableFrom(m).length));
  const fresh = act.filter(m => m.released && NOW - Date.parse(m.released) < 30 * DAY).sort((a, b) => b.released.localeCompare(a.released));
  const ending = ms.filter(m => m.eol && daysTo(m.eol) >= 0 && daysTo(m.eol) <= 90);
  const mine = act.filter(m => avail(m, S.region) !== 'no');
  $('#tiles').innerHTML = [
    [act.length, 'active models (on-demand or profile)'], [new Set(act.map(m => m.provider)).size, 'providers'],
    [mine.length, `callable from ${S.region}`],
    [fresh.length, `released in 30 days${fresh.length ? ': ' + fresh.slice(0, 2).map(m => esc(m.name)).join(', ') : ''}`],
    [ending.length, 'reach end of life within 90 days', ending.length ? 'warn' : ''],
  ].map(([b, s, c]) => `<div class="tile ${c || ''}"><b>${b}</b><span>${s}</span></div>`).join('');
}

function quick() {
  $('#q-region-label').textContent = S.region;
  const q = $('#q-model').value.trim().toLowerCase(), box = $('#q-answer');
  if (!q) { box.innerHTML = ''; return; }
  const m = Object.values(C.models).find(x => x.name?.toLowerCase() === q || x.id.toLowerCase() === q)
    || Object.values(C.models).filter(x => x.status !== 'LEGACY').find(x => (x.name + ' ' + x.id).toLowerCase().includes(q));
  if (!m) { box.innerHTML = '<p class="sub">No model matches that.</p>'; return; }
  box.innerHTML = `<p><b>${esc(m.name)}</b> <span class="sub">${esc(m.provider)}</span> · <a href="#model=${encodeURIComponent(m.id)}">full details</a></p>` + idList(m, S.region, true);
}

function idList(m, r, withNotes) {
  const ids = callIds(m, r);
  if (!ids.length) {
    const where = callableFrom(m);
    return `<p>Not callable from <b>${r}</b>.${where.length ? ` Callable from: ${where.map(x => `<a href="#" data-region="${x}">${x}</a>`).join(', ')}.` : ''}</p>`;
  }
  return '<div class="ids">' + ids.map((x, i) => `<div class="id-row${i === 0 ? ' best' : ''}">
      <span class="mono">${esc(x.id)}</span><button class="copy" data-copy="${esc(x.id)}">Copy</button>
      <small>${i === 0 ? '<b>Use this</b> · ' : ''}${kindNote(x)}</small></div>`).join('') + '</div>'
    + (withNotes ? notesBlock(m, true) : '');
}

function notesBlock(m, compact) {
  let n = N[m.id];
  if (n && n.same_as) n = {...N[n.same_as], measured: n.measured, same_as: n.same_as};
  const g = gotchas(m);
  let html = '';
  if (g.length && !compact) html += '<ul class="notes">' + g.map(([c, t]) => `<li class="${c === 'info' ? 'info' : ''}">${t}</li>`).join('') + '</ul>';
  if (n && n.rows) {
    const rows = compact ? n.rows.filter(r => r[0] === 'no').slice(0, 4) : n.rows;
    html += `<h3>${compact ? 'Measured on Bedrock' : 'Deeper notes'}${n.measured ? ' · ' + n.measured : ''}${n.same_as ? ` (same results as ${esc(n.same_as)})` : ''}</h3><ul class="notes">`
      + rows.map(([s, what, detail]) => `<li class="${s === 'no' ? '' : 'info'}"><b>${s === 'no' ? 'Rejected' : s === 'ok' ? 'Works' : 'Note'}:</b> ${esc(what)}${detail ? ` — <span class="sub">${esc(detail)}</span>` : ''}</li>`).join('')
      + '</ul>' + (compact && n.rows.length > rows.length ? `<p class="sub"><a href="#model=${encodeURIComponent(m.id)}">${n.rows.length - rows.length} more measured rows</a></p>` : '');
  } else if (compact && g.some(x => x[0] === 'warn')) {
    html += '<ul class="notes">' + g.filter(x => x[0] === 'warn').map(([, t]) => `<li>${t}</li>`).join('') + '</ul>';
  }
  return html;
}

function feats(m) {
  const f = [];
  if (m.input.includes('IMAGE')) f.push('image');
  if (m.documents.length) f.push('docs');
  if (m.input.includes('VIDEO') || m.videos.length) f.push('video');
  if (m.prompt_caching) f.push('caching');
  if (m.reasoning_field) f.push('reasoning');
  if (m.openai_chat || m.openai_responses) f.push('OpenAI API');
  if (m.batch) f.push('batch');
  if (!m.input.includes('TEXT') || !m.output.includes('TEXT')) f.push(m.output.join('+').toLowerCase());
  return '<div class="feat">' + f.map(x => `<span class="pill">${esc(x)}</span>`).join('') + '</div>';
}

function modelsTab() {
  const q = $('#search').value.trim().toLowerCase(), prov = $('#provider').value;
  const tests = CHIPS.filter(c => S.chips.has(c[0])).map(c => c[2]);
  let ms = Object.values(C.models).filter(m =>
    (!q || (m.name + ' ' + m.id).toLowerCase().includes(q)) && (!prov || m.provider === prov)
    && tests.every(t => t(m)) && (S.chips.has('legacy') || m.status !== 'LEGACY') && (m.pending || callableFrom(m).length));
  ms.sort((a, b) => (b.released || '').localeCompare(a.released || '') || a.name.localeCompare(b.name));
  const hidden = Object.values(C.models).filter(m => !m.pending && !callableFrom(m).length).length;
  $('#count').textContent = `${ms.length} models · availability shown for ${S.region} · ${hidden} variants with no on-demand or profile access (provisioned throughput only) are hidden`;
  $('#models').innerHTML = `<thead><tr><th>Model</th><th>Provider</th><th>Released</th><th>${S.region}</th><th class="num">Max output</th><th>Supports</th></tr></thead><tbody>`
    + ms.map(m => `<tr data-model="${esc(m.id)}"><td><b>${esc(m.name)}</b>${m.status === 'LEGACY' ? ' <span class="pill legacy">Legacy</span>' : m.released && NOW - Date.parse(m.released) < 30 * DAY ? ' <span class="pill new">New</span>' : ''}<span class="mono">${esc(m.id)}</span></td>
      <td>${esc(m.provider)}</td><td class="num">${fmtDate(m.released)}</td><td>${pill(avail(m, S.region))}</td><td class="num">${k(m.max_tokens)}</td><td>${feats(m)}</td></tr>`).join('') + '</tbody>';
}

const PLABEL = {system: 'system prompt', temperature: 'temperature 0.5', top_p: 'topP 0.9', stop_sequences: 'stopSequences', tool_auto: 'tools (auto)', tool_forced: 'forced tool (any)', cache_point: 'cachePoint', prefill: 'assistant prefill'};
function paramsTab() {
  if (!P) { $('#params').innerHTML = '<tbody><tr><td>No measurements yet.</td></tr></tbody>'; return; }
  const prov = $('#p-provider').value;
  const rows = Object.entries(P.models).map(([id, r]) => [C.models[id], r]).filter(([m]) => m && (!prov || m.provider === prov))
    .sort(([a], [b]) => a.provider.localeCompare(b.provider) || (b.released || '').localeCompare(a.released || ''));
  const ans = rows.filter(([, r]) => !r.baseline);
  $('#p-sub').textContent = `One Converse request per cell, maxTokens 16, ${P.region}, measured ${P.measured_at.replace('T', ' ')}. ${ans.length} of ${rows.length} models answered; the rest need model access or a Marketplace agreement on the probing account. Accepted means no error, not that the setting had an effect.`;
  let html = `<thead><tr><th>Model</th>${P.probes.map(p => `<th class="reg">${PLABEL[p] || p}</th>`).join('')}</tr></thead><tbody>`, last = '';
  for (const [m, r] of rows) {
    if (m.provider !== last) { html += `<tr class="prov"><td colspan="${P.probes.length + 1}">${esc(m.provider)}</td></tr>`; last = m.provider; }
    html += `<tr><td class="name" data-model="${esc(m.id)}" title="called as ${esc(r.via)}">${esc(m.name)}</td>` + (r.baseline
      ? `<td class="na" colspan="${P.probes.length}" title="${esc(r.baseline)}">not measured: ${esc(r.baseline.slice(0, 70))}</td>`
      : P.probes.map(p => { const [ok, err] = r.results[p] || [null, '']; return `<td><span class="cell ${ok ? 'od' : 'bad'}" title="${esc(m.name)} · ${esc(PLABEL[p] || p)}: ${ok ? 'accepted' : esc(err)}">${ok ? '✓' : '✕'}</span></td>`; }).join('')) + '</tr>';
  }
  $('#params').innerHTML = html + '</tbody>';
}

function probeBlock(m) {
  const r = P && P.models[m.id];
  if (!r || r.baseline) return '';
  const bad = P.probes.filter(p => !r.results[p][0]);
  return `<h3>Measured ${P.measured_at.slice(0, 10)} · ${esc(r.via)} in ${P.region}</h3><ul class="notes">` +
    P.probes.map(p => { const [ok, err] = r.results[p]; return `<li class="${ok ? 'info' : ''}"><b>${ok ? 'Accepted' : 'Rejected'}:</b> ${PLABEL[p]}${ok ? '' : ` — <span class="sub">${esc(err)}</span>`}</li>`; }).join('') + '</ul>';
}

function mapTab() {
  const prov = $('#map-provider').value, legacy = $('#map-legacy').checked;
  const ms = Object.values(C.models).filter(m => (!prov || m.provider === prov) && (legacy || m.status !== 'LEGACY') && callableFrom(m).length)
    .sort((a, b) => a.provider.localeCompare(b.provider) || (b.released || '').localeCompare(a.released || ''));
  const regs = C.regions;
  const counts = regs.map(r => ms.filter(m => avail(m, r) !== 'no').length);
  let html = `<thead><tr><th>Model</th>${regs.map((r, i) => `<th class="reg${r === S.region ? ' mine' : ''}" title="${counts[i]} models">${r} · ${counts[i]}</th>`).join('')}</tr></thead><tbody>`;
  let last = '';
  for (const m of ms) {
    if (m.provider !== last) { html += `<tr class="prov"><td colspan="${regs.length + 1}">${esc(m.provider)}</td></tr>`; last = m.provider; }
    html += `<tr><td class="name" data-model="${esc(m.id)}" title="${esc(m.id)}">${esc(m.name)}</td>` + regs.map(r => {
      const a = avail(m, r);
      return `<td class="${r === S.region ? 'mine' : ''}"><span class="cell ${a}" title="${esc(m.name)} in ${r}: ${a === 'od' ? 'on-demand' : a === 'ip' ? 'inference profile only' : 'not offered'}">${a === 'od' ? '●' : a === 'ip' ? '◐' : ''}</span></td>`;
    }).join('') + '</tr>';
  }
  $('#map').innerHTML = html + '</tbody>';
}

function feedTab() {
  const win = +$('#new-window').value * DAY, items = [];
  for (const m of Object.values(C.models))
    if (m.released && NOW - Date.parse(m.released) < win) items.push({t: m.released, kind: 'launch', m});
  const flap = new Set(), lastSeen = {};
  for (const e of H.events) for (const [r, sign] of [...e.added.map(r => [r, 1]), ...e.removed.map(r => [r, -1])]) {
    const key = e.model + '|' + r, p = lastSeen[key];
    if (p && p.sign !== sign && Date.parse(e.t) - Date.parse(p.t) < 3 * DAY) { flap.add(p.t + key); flap.add(e.t + key); delete lastSeen[key]; }
    else lastSeen[key] = {t: e.t, sign};
  }
  for (const e0 of H.events) {
    const e = {...e0, added: e0.added.filter(r => !flap.has(e0.t + e0.model + '|' + r)), removed: e0.removed.filter(r => !flap.has(e0.t + e0.model + '|' + r))};
    if (!e.added.length && !e.removed.length) continue;
    if (NOW - Date.parse(e.t) > win) continue;
    const m = C.models[e.model];
    if (m && m.status === 'LEGACY') continue;
    items.push({t: e.t, kind: 'regions', e, m});
  }
  items.sort((a, b) => b.t.localeCompare(a.t));
  $('#feed').innerHTML = items.map(x => {
    const name = x.m ? esc(x.m.name) : esc(x.e.model), id = x.m ? x.m.id : x.e.model;
    if (x.kind === 'launch') return `<li><time>${fmtDate(x.t)}</time><div class="what"><span class="pill new">Released</span> <b data-model="${esc(id)}">${name}</b> <span class="sub">${esc(x.m.provider)}</span>
      <div class="regs">Callable from ${callableFrom(x.m).length} of ${C.regions.length} tracked regions · ${S.region}: ${pill(avail(x.m, S.region))}</div></div></li>`;
    const a = x.e.added, r = x.e.removed;
    return `<li><time>${fmtDate(x.t)}</time><div class="what">${a.length ? `<span class="pill od">+${a.length} region${a.length > 1 ? 's' : ''}</span>` : ''} ${r.length ? `<span class="pill legacy">−${r.length}</span>` : ''} <b data-model="${esc(id)}">${name}</b>
      <div class="regs">${a.length ? 'Listed in ' + a.join(', ') : ''}${a.length && r.length ? ' · ' : ''}${r.length ? 'No longer listed in ' + r.join(', ') : ''}</div></div></li>`;
  }).join('') || '<li><span></span><span class="sub">Nothing in this window.</span></li>';
}

function lifeTab() {
  const ms = Object.values(C.models).filter(m => m.status === 'LEGACY' || m.eol)
    .sort((a, b) => (a.eol || '9').localeCompare(b.eol || '9'));
  $('#life').innerHTML = `<thead><tr><th>Model</th><th>Provider</th><th class="num">Legacy since</th><th class="num">Extended access from</th><th class="num">End of life</th><th class="num">Days left</th></tr></thead><tbody>`
    + ms.map(m => { const d = daysTo(m.eol);
      return `<tr data-model="${esc(m.id)}"><td><b>${esc(m.name)}</b><span class="mono">${esc(m.id)}</span></td><td>${esc(m.provider)}</td>
      <td class="num">${fmtDate(m.legacy)}</td><td class="num">${fmtDate(m.extended)}</td><td class="num">${fmtDate(m.eol)}</td>
      <td class="num"><span class="days ${d != null && d <= 30 ? 'soon' : ''}">${d == null ? '—' : d < 0 ? 'ended' : (d <= 30 ? '⚠ ' : '') + d}</span></td></tr>`; }).join('') + '</tbody>';
}

function detail(id) {
  const m = C.models[id];
  if (!m) return;
  $('#d-title').textContent = m.name;
  $('#d-sub').innerHTML = `<span class="mono">${esc(m.id)}</span> · ${esc(m.provider)}${m.family ? ' · ' + esc(m.family) : ''} · released ${fmtDate(m.released)} ${m.status === 'LEGACY' ? '<span class="pill legacy">Legacy</span>' : ''}`;
  const first = {};
  for (const e of H.events) if (e.model === id) for (const r of e.added) first[r] = first[r] || e.t;
  const ids = callIds(m, S.region);
  const kv = [['Input', m.input.join(', ').toLowerCase()], ['Output', m.output.join(', ').toLowerCase()], ['Max output', m.max_tokens ? m.max_tokens.toLocaleString() : '—'],
    ['Images', m.images.join(', ') || '—'], ['Documents', m.documents.join(', ') || '—'], ['Streaming', m.streaming ? 'yes' : 'no'],
    ['Prompt caching', m.prompt_caching ? 'yes' : 'no'], ['Count tokens API', m.count_tokens ? 'yes' : 'no'], ['Batch', m.batch ? 'yes' : 'no'],
    ['Guardrails', m.guardrails ? 'yes' : 'no'], ['OpenAI Chat / Responses', `${m.openai_chat ? 'yes' : 'no'} / ${m.openai_responses ? 'yes' : 'no'}`],
    ['Fine-tuning', m.customization.join(', ').toLowerCase() || 'no']];
  $('#d-body').innerHTML = `
    <h3>Call it from <select id="d-region">${C.regions.map(r => `<option${r === S.region ? ' selected' : ''}>${r}</option>`).join('')}</select></h3>
    <div id="d-ids">${idList(m, S.region, false)}</div>
    ${ids.length ? `<h3>Python (boto3)</h3><div class="snip"><button class="copy" data-copy-pre="1">Copy</button><pre id="d-snip">${esc(snippet(m, ids[0].id, S.region))}</pre></div>` : ''}
    ${probeBlock(m)}
    ${notesBlock(m, false)}
    <h3>Capabilities (from the Bedrock API)</h3><div class="kv">${kv.map(([a, b]) => `<div><span>${a}</span><b>${esc(b)}</b></div>`).join('')}</div>
    <h3>Regions</h3><div class="reg-grid">${C.regions.map(r => { const a = avail(m, r);
      return `<div class="${r === S.region ? 'mine' : ''}"><span>${r}</span><span title="${first[r] ? 'first listed ' + fmtDate(first[r]) : ''}">${a === 'od' ? '● on-demand' : a === 'ip' ? '◐ profile' : '—'}</span></div>`; }).join('')}</div>
    ${m.status === 'LEGACY' ? `<h3>Lifecycle</h3><p>Legacy since ${fmtDate(m.legacy)} · extended access ${fmtDate(m.extended)} · end of life <b>${fmtDate(m.eol)}</b> (${daysTo(m.eol)} days)</p>` : ''}
    <p class="sub">Permalink: <a href="#model=${encodeURIComponent(m.id)}&region=${S.region}">#model=${esc(m.id)}</a></p>`;
  $('#d-region').onchange = e => { setRegion(e.target.value); detail(id); };
  const dlg = $('#detail');
  if (!dlg.open) dlg.showModal();
}

/* ---------- wiring ---------- */
function render() {
  tiles(); quick();
  ({models: modelsTab, params: paramsTab, regions: mapTab, new: feedTab, lifecycle: lifeTab})[S.tab]();
  document.querySelectorAll('.tabs button').forEach(b => b.setAttribute('aria-selected', b.dataset.tab === S.tab));
  document.querySelectorAll('.tab').forEach(t => t.hidden = t.id !== 'tab-' + S.tab);
}
function setRegion(r) {
  if (!C.regions.includes(r)) return;
  S.region = r; $('#region').value = r; localStorage.setItem('bedrock-region', r); render();
}
function readHash() {
  const h = new URLSearchParams(location.hash.slice(1));
  if (h.get('region')) setRegion(h.get('region'));
  if (h.get('tab')) { S.tab = h.get('tab'); render(); }
  if (h.get('model')) detail(h.get('model'));
}

async function main() {
  const get = u => fetch(u).then(r => r.ok ? r.json() : null).catch(() => null);
  const [cat, hist, notes, probes, live] = await Promise.all([get('data/catalog.json'), get('data/history.json'), get('data/notes.json'), get('data/probes.json'), get(LIVE)]);
  if (!cat) { document.querySelector('main').innerHTML = '<p>Could not load data/catalog.json.</p>'; return; }
  C = cat; H = hist || {events: []}; N = notes || {}; P = probes;
  for (const [id, m] of Object.entries(C.models)) {
    m.id = id;
    const v = id.match(/:(\d+k|\d+m|mm)$/i);  // context-length / provisioned variants share the display name
    if (v) m.name += ` (${v[1]})`;
  }
  let pending = 0;
  if (live) for (const [prov, ms] of Object.entries(live.providers || {}))  // newer than the catalog: show what we know
    for (const [id, v] of Object.entries(ms)) if (!C.models[id]) {
      pending++;
      C.models[id] = {id, name: id + ' (details pending)', provider: prov, input: [], output: [], images: [], documents: [], videos: [], customization: [], reasoning_levels: [],
        status: 'ACTIVE', released: null, pending: true, regions: Object.fromEntries((v.regions || []).filter(r => C.regions.includes(r)).map(r => [r, ['INFERENCE_PROFILE']])), profiles: []};
    }
  $('#freshness').textContent = `Catalog rebuilt ${C.generated_at.replace('T', ' ').replace('Z', ' UTC')} from ${C.regions.length} regions` +
    (live ? ` · region list checked ${live.generated_at}` : '') + (pending ? ` · ${pending} model(s) seen since the last rebuild, details pending` : '') +
    (Object.keys(C.skipped_regions || {}).length ? ` · not covered: ${Object.keys(C.skipped_regions).join(', ')}` : '');

  const saved = localStorage.getItem('bedrock-region');
  if (saved && C.regions.includes(saved)) S.region = saved;
  $('#region').innerHTML = C.regions.map(r => `<option>${r}</option>`).join(''); $('#region').value = S.region;
  const provs = [...new Set(Object.values(C.models).map(m => m.provider))].sort();
  for (const sel of ['#provider', '#map-provider', '#p-provider']) $(sel).innerHTML += provs.map(p => `<option>${esc(p)}</option>`).join('');
  $('#model-list').innerHTML = Object.values(C.models).filter(m => m.status !== 'LEGACY').map(m => `<option value="${esc(m.name)}">${esc(m.id)}</option>`).join('');
  $('#chips').innerHTML = CHIPS.map(([id, label]) => `<button class="chip" data-chip="${id}" aria-pressed="false">${label}</button>`).join('');

  $('#region').onchange = e => setRegion(e.target.value);
  $('#q-model').oninput = quick;
  for (const id of ['#search', '#provider']) $(id).oninput = modelsTab;
  for (const id of ['#map-provider', '#map-legacy']) $(id).onchange = mapTab;
  $('#new-window').onchange = feedTab;
  $('#p-provider').onchange = paramsTab;
  $('#d-close').onclick = () => $('#detail').close();
  $('#detail').addEventListener('close', () => { if (location.hash.includes('model=')) history.replaceState(null, '', location.pathname + (S.tab !== 'models' ? '#tab=' + S.tab : '')); });
  document.addEventListener('click', e => {
    const t = e.target.closest('[data-tab],[data-chip],[data-model],[data-copy],[data-copy-pre],[data-region]');
    if (!t) return;
    if (t.dataset.tab) { S.tab = t.dataset.tab; history.replaceState(null, '', '#tab=' + S.tab); render(); }
    else if (t.dataset.chip) { S.chips.has(t.dataset.chip) ? S.chips.delete(t.dataset.chip) : S.chips.add(t.dataset.chip); t.setAttribute('aria-pressed', S.chips.has(t.dataset.chip)); modelsTab(); }
    else if (t.dataset.model) { history.replaceState(null, '', '#model=' + encodeURIComponent(t.dataset.model)); detail(t.dataset.model); }
    else if (t.dataset.region) { e.preventDefault(); setRegion(t.dataset.region); }
    else {
      navigator.clipboard?.writeText(t.dataset.copy || $('#d-snip').textContent);
      const old = t.textContent; t.textContent = 'Copied'; setTimeout(() => t.textContent = old, 1200);
    }
  });
  window.addEventListener('hashchange', readHash);
  render(); readHash();
}
main();
