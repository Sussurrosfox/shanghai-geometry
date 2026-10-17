
function renderMath(target) {
  if (typeof renderMathInElement === 'function') {
    renderMathInElement(target || document.body, {
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
  // 监听动态步骤切换导致的 DOM 变动，自动重新渲染数学公式
  let mathTimer = null;
  const observer = new MutationObserver(() => {
    if (mathTimer) clearTimeout(mathTimer);
    mathTimer = setTimeout(renderMath, 30);
  });
  observer.observe(document.body, { childList: true, subtree: true });
});
window.addEventListener('load', renderMath);
