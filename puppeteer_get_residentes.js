const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto('https://www.autocompara.com', { waitUntil: 'networkidle2' });

  console.log("🔄 Esperando a que el sitio cargue completamente...");
  await new Promise(resolve => setTimeout(resolve, 5000)); // puedes subir el tiempo si la página tarda

  const cookies = await page.cookies();
  const cookieString = cookies.map(c => `${c.name}=${c.value}`).join('; ');

  fs.writeFileSync('cookies_autocompara.txt', cookieString, 'utf8');
  console.log("✅ Cookies guardadas en cookies_autocompara.txt");

  await browser.close();
})();
