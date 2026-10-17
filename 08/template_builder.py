import os, sys, math, json

# 确保输出 UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def gen_html_template(title, subtitle, problem_md, view_box, base_svg, pts_svg, step_defs, js_extra=""):
    """
    通用标准三层 SVG 交互页面模版
    """
    cards_html = ""
    for s in step_defs:
        idx = s['step']
        t = s['title']
        p = s['text']
        active = " active" if idx == 0 else ""
        cards_html += f"""
        <div class="step-card{active}" id="card-{idx}" onclick="setStep({idx})">
          <div class="step-badge">步骤 {idx}</div>
          <div class="step-title">{t}</div>
          <div class="step-body">{p}</div>
        </div>
        """

    steps_json = json.dumps(step_defs, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — 几何证明交互演示</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Microsoft YaHei", sans-serif;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    min-height: 100vh;
    color: #1e293b;
    padding: 20px 16px;
    display: flex;
    flex-direction: column;
  }}
  .container {{ max-width: 1240px; margin: 0 auto; width: 100%; display: flex; flex-direction: column; gap: 16px; }}
  header {{ background: #fff; padding: 18px 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }}
  h1 {{ font-size: 20px; font-weight: 700; color: #0f172a; margin-bottom: 6px; }}
  .subtitle {{ font-size: 14px; color: #64748b; line-height: 1.5; }}
  .main-content {{ display: grid; grid-template-columns: 420px 1fr; gap: 16px; align-items: start; }}
  @media (max-width: 900px) {{ .main-content {{ grid-template-columns: 1fr; }} }}
  .panel-left {{ display: flex; flex-direction: column; gap: 12px; max-height: 700px; }}
  .steps-container {{
    display: flex; flex-direction: column; gap: 10px; overflow-y: auto; padding-right: 4px;
    max-height: 560px;
  }}
  .step-card {{
    background: #fff; border: 2px solid #e2e8f0; border-radius: 10px; padding: 14px;
    cursor: pointer; transition: all 0.2s ease;
  }}
  .step-card:hover {{ border-color: #cbd5e1; transform: translateY(-1px); }}
  .step-card.active {{ border-color: #2563eb; background: #eff6ff; box-shadow: 0 4px 6px -1px rgba(37,99,235,0.1); }}
  .step-badge {{ font-size: 11px; font-weight: 700; color: #2563eb; text-transform: uppercase; margin-bottom: 4px; }}
  .step-title {{ font-size: 15px; font-weight: 600; color: #0f172a; margin-bottom: 6px; }}
  .step-body {{ font-size: 13px; color: #475569; line-height: 1.6; }}
  .panel-right {{
    background: #fff; border-radius: 12px; padding: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
    display: flex; flex-direction: column; gap: 12px; align-items: center;
  }}
  .svg-wrap {{
    width: 100%; max-width: 680px; height: 560px; background: #ffffff; border: 1px solid #e2e8f0;
    border-radius: 8px; display: flex; align-items: center; justify-content: center;
  }}
  svg {{ width: 100%; height: 100%; }}
  .controls {{
    display: flex; gap: 8px; align-items: center; justify-content: center; width: 100%;
    padding-top: 4px; flex-wrap: wrap;
  }}
  .btn {{
    padding: 8px 16px; border-radius: 6px; font-size: 13px; font-weight: 600; cursor: pointer;
    border: none; background: #2563eb; color: #fff; transition: background 0.15s ease;
  }}
  .btn:hover {{ background: #1d4ed8; }}
  .btn.secondary {{ background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }}
  .btn.secondary:hover {{ background: #e2e8f0; }}
  .step-info {{ font-size: 13px; font-weight: 600; color: #64748b; margin: 0 8px; }}
</style>
</head>
<body>
<div class="container">
  <header>
    <h1>{title}</h1>
    <div class="subtitle">{subtitle}</div>
  </header>
  <div class="main-content">
    <div class="panel-left">
      <div class="steps-container">
        {cards_html}
      </div>
    </div>
    <div class="panel-right">
      <div class="svg-wrap">
        <svg id="geoSvg" viewBox="{view_box}">
          <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
            </marker>
          </defs>
          <g id="gBase">{base_svg}</g>
          <g id="gStep"></g>
          <g id="gPts">{pts_svg}</g>
        </svg>
      </div>
      <div class="controls">
        <button class="btn secondary" onclick="prevStep()">上一步</button>
        <span class="step-info" id="stepIndicator">步骤 0 / {len(step_defs)-1}</span>
        <button class="btn" onclick="nextStep()">下一步</button>
        <button class="btn secondary" id="autoBtn" onclick="toggleAuto()">自动播放</button>
        <button class="btn secondary" onclick="setStep(0)">重置</button>
      </div>
    </div>
  </div>
</div>
<script>
const STEPS = {steps_json};
let curStep = 0;
let autoTimer = null;

function setStep(idx) {{
  if (idx < 0) idx = 0;
  if (idx >= STEPS.length) idx = STEPS.length - 1;
  curStep = idx;

  document.querySelectorAll('.step-card').forEach((c, i) => {{
    c.classList.toggle('active', i === curStep);
    if (i === curStep) c.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
  }});

  document.getElementById('stepIndicator').innerText = `步骤 ${{curStep}} / ${{STEPS.length - 1}}`;
  const gStep = document.getElementById('gStep');
  gStep.innerHTML = STEPS[curStep].svg || '';

  // 绑定 URL
  const url = new URL(window.location);
  url.searchParams.set('step', curStep);
  window.history.replaceState({{}}, '', url);

  if (window.onStepChanged) window.onStepChanged(curStep);
}}

function nextStep() {{ setStep(curStep + 1); }}
function prevStep() {{ setStep(curStep - 1); }}

function toggleAuto() {{
  const btn = document.getElementById('autoBtn');
  if (autoTimer) {{
    clearInterval(autoTimer);
    autoTimer = null;
    btn.innerText = '自动播放';
  }} else {{
    btn.innerText = '暂停播放';
    autoTimer = setInterval(() => {{
      if (curStep >= STEPS.length - 1) {{
        setStep(0);
      }} else {{
        nextStep();
      }}
    }}, 2600);
  }}
}}

window.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === ' ') {{ nextStep(); }}
  else if (e.key === 'ArrowLeft') {{ prevStep(); }}
}});

window.addEventListener('DOMContentLoaded', () => {{
  const p = new URLSearchParams(window.location.search);
  const s = parseInt(p.get('step') || '0', 10);
  setStep(isNaN(s) ? 0 : s);
}});

{js_extra}
</script>
</body>
</html>
"""
    return html

print("Template builder loaded successfully.")
