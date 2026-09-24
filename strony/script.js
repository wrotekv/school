function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function typeTitle(text) {
  for (let i = 1; i <= text.length; i++) {
    document.title = text.slice(0, i);
    await sleep(200);
    if (i == text.length) {
      i = 0;
      await sleep(200);
    }
  }
}

typeTitle("larper");
