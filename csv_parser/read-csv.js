const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

function Tmp(Номер, Аспект, Требование_ТЗ, Текущий_макет, Критичность) {
  this.N = Номер;
  this.Аспект = Аспект;
  this.Требование_ТЗ = Требование_ТЗ;
  this.Текущий_макет = Текущий_макет;
  this.Критичность = Критичность;
}

const results = [];

fs.createReadStream(path.join(__dirname, 'table_косяков.csv'))
  .pipe(csv({
    separator: ';',
    mapHeaders: ({ header }) => header.trim(),
    mapValues: ({ value }) => value.trim()
  }))
  .on('data', (row) => {
    results.push(new Tmp(
      row.Номер,
      row.Аспект,
      row.Требование_ТЗ,
      row.Текущий_макет,
      row.Критичность
    ));
  })
  .on('end', () => {
    console.log('✅ Данные успешно загружены из CSV:');
    console.table(results);
  })
  .on('error', (err) => {
    console.error('❌ Ошибка при чтении CSV:', err.message);
  });
