const board = document.getElementById('board');
const statusEl = document.getElementById('status');
const resetBtn = document.getElementById('reset');

function render(game) {
  const cells = board.querySelectorAll('.cell');
  cells.forEach((cell, i) => {
    const val = game.board[i];
    cell.textContent = val || '';
    cell.className = 'cell' + (val ? ' ' + val.toLowerCase() : '');
    cell.disabled = !!val || !!game.winner || !!game.draw;
  });

  if (game.winner) {
    statusEl.textContent = `Player ${game.winner} wins!`;
  } else if (game.draw) {
    statusEl.textContent = "It's a draw!";
  } else {
    statusEl.textContent = `Player ${game.turn}'s turn`;
  }
}

board.addEventListener('click', async (e) => {
  const cell = e.target.closest('.cell');
  if (!cell) return;
  const index = parseInt(cell.dataset.index, 10);
  const res = await fetch('/move', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ index }),
  });
  const game = await res.json();
  render(game);
});

resetBtn.addEventListener('click', async () => {
  const res = await fetch('/reset', { method: 'POST' });
  const game = await res.json();
  render(game);
});

fetch('/').then(r => r.text()).then(html => {
  const match = html.match(/<p id="status"[^>]*>([^<]*)<\/p>/);
  if (match) statusEl.textContent = match[1];
});
