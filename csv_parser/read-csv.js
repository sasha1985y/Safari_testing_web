const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

function Tmp(Номер, Браузер, Разрешение, Проблема, Описание) {
  this.N = Номер;
  this.Браузер = Браузер;
  this.Разрешение = Разрешение;
  this.Проблема = Проблема;
  this.Описание = Описание;
}

const results = [];

fs.createReadStream(path.join(__dirname, 'test-data.csv'))
  .pipe(csv({
    separator: ',',
    mapHeaders: ({ header }) => header.trim(),
    mapValues: ({ value }) => value.trim()
  }))
  .on('data', (row) => {
    results.push(new Tmp(
      row.Номер,
      row.Браузер,
      row.Разрешение,
      row.Проблема,
      row.Описание
    ));
  })
  .on('end', () => {
    console.log('✅ Данные успешно загружены из CSV:');
    console.table(results);
  })
  .on('error', (err) => {
    console.error('❌ Ошибка при чтении CSV:', err.message);
  });
