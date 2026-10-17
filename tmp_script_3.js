
function renderMath(target) {
  if (typeof renderMathInElement === 'function') {
    const el = (target && target.nodeType) ? target : document.body;
    renderMathInElement(el, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\(', right: '\)', display: false},
        {left: '\[', right: '\]', display: true}
      ],
      macros: {
        '\parallel': '\mathbin{/\!/}',
        '\bigtriangleup': '\triangle'
      },
      throwOnError: false
    });
  }
}
window.addEventListener('DOMContentLoaded', () => {
  renderMath();
  let mathTimer = null;
  const observer = new MutationObserver(() => {
    if (mathTimer) clearTimeout(mathTimer);
    mathTimer = setTimeout(renderMath, 30);
  });
  observer.observe(document.body, { childList: true, subtree: true });
});
window.addEventListener('load', () => renderMath());
