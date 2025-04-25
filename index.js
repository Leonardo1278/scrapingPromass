const axios = require('axios');
const fs = require('fs');
const path = require('path');

let modelos = [];
let formasPago = [];
let available_socios = [];
let available_deducibles = [];
let available_planes = [];
let available_profesiones = [];
let available_nacionalidades = [];

const headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
  'Referer': 'https://www.autocompara.com/',
  'Origin': 'https://www.autocompara.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Connection': 'keep-alive'
};

const getModelosPorAño = async (año) => {
  try {
    const response = await axios.get(`https://www.autocompara.com/autocompara/v1/catalogosfnx/vehiculos/1/${año}`, { headers });
    if (response.data.length === 0) {
      console.log(`❌ Año ${año} no tiene modelos disponibles.`);
      return;
    }

    console.log(`\nModelos disponibles en ${año}:`);
    response.data.forEach(m => {
      console.log(`- ${m.marca}`);
      modelos.push({
        idMarca: año,
        version: m.version,
        marca: m.marca
      });
    });
  } catch (error) {
    console.warn(`❌ Error en el año ${año}:`, error.message);
  }
};

const getFormasPago = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/catalogos/formaPago', { headers });
    formasPago = response.data;
    console.log(`\n✅ Formas de pago obtenidas: ${formasPago.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener formas de pago:", error.message);
  }
};

const getSocio = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/catalogos/socio', { headers });
    available_socios = response.data;
    console.log(`\n✅ Socios obtenidos: ${available_socios.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener socios:", error.message);
  }
};

const getDeducibles = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/vehiculos/deducibles/43974597', { headers });
    available_deducibles = response.data.map(d => ({
      codigo: d.codigo,
      cobertura: d.cobertura,
      valdef: d.valdef,
      deducibles: JSON.stringify(d.deducibles)
    }));
    console.log(`\n✅ Deducibles obtenidos: ${available_deducibles.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener deducibles:", error.message);
  }
};

const getPlan = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/catalogos/plan', { headers });
    available_planes = response.data;
    console.log(`\n✅ Planes obtenidos: ${available_planes.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener planes:", error.message);
  }
};

const getProfesion = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/catalogos/profesion', { headers });
    available_profesiones = response.data;
    console.log(`\n✅ Profesiones obtenidas: ${available_profesiones.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener profesiones:", error.message);
  }
};

const getNacionalidad = async () => {
  try {
    const response = await axios.get('https://www.autocompara.com/autocompara/v1/catalogosfnx/catalogos/nacionalidad', { headers });
    available_nacionalidades = response.data;
    console.log(`\n✅ Nacionalidades obtenidas: ${available_nacionalidades.length}`);
  } catch (error) {
    console.warn("❌ Error al obtener nacionalidades:", error.message);
  }
};




const guardarCSV = () => {
  fs.writeFileSync(path.join(__dirname, 'modelos_autocompara.csv'), 'idMarca,version,marca\n' + modelos.map(m => `${m.idMarca},"${m.version}","${m.marca}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'formas_pago_autocompara.csv'), 'id,nombre\n' + formasPago.map(p => `${p.id},"${p.valor}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'socios.csv'), 'id,Socio\n' + available_socios.map(s => `${s.id},"${s.valor}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'deducibles.csv'), 'codigo,cobertura,valdef,deducibles\n' + available_deducibles.map(d => `${d.codigo},"${d.cobertura}","${d.valdef}","${d.deducibles}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'planes.csv'), 'id,Plan\n' + available_planes.map(p => `${p.id},"${p.valor}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'profesiones.csv'), 'id,Profesion\n' + available_profesiones.map(p => `${p.id},"${p.valor}"`).join('\n'), 'utf8');
  fs.writeFileSync(path.join(__dirname, 'nacionalidades.csv'), 'id,Nacionalidad\n' + available_nacionalidades.map(n => `${n.id},"${n.valor}"`).join('\n'), 'utf8');
  console.log(`\n✅ Archivos CSV guardados correctamente.`);
};

const main = async () => {
  for (let año = 1960; año <= 2025; año++) {
    await getModelosPorAño(año);
  }
  await getFormasPago();
  await getSocio();
  await getDeducibles();
  await getPlan();
  await getProfesion();
  await getNacionalidad();
  guardarCSV();
};

main();
