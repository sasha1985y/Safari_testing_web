
// function Tmp(Номер, Браузер, Разрешение, Проблема, Описание) {
//   this.N = Номер;
//   this.Браузер = Браузер;
//   this.Разрешение = Разрешение;
//   this.Проблема = Проблема;
//   this.Описание = Описание;
// }

// const INT = 8;
// const data = [];

// for (let i = 1; i < INT; i++) {
//   const args = Array(Tmp.length - 1).fill('mocks');
//   data.push(new Tmp(i, ...args));
// }

// console.table(data);
// tmpRange(INT);
//______________________________________________________________________
// function Tmp(Браузер, Разрешение, Проблема, Описание) {
// this.Браузер = Браузер;
//   this.Разрешение = Разрешение;
//   this.Проблема = Проблема;
//   this.Описание = Описание;
// }

// const INT = 8;
// for (var i = 1; i < INT; i++) {
//   const args = Array(Tmp.length).fill('""').join(', ');
//   console.log(`var tmp${i} = new Tmp(${args});`);
// }

// function tmpRange(int) {
//    let arr = [];
//    for (var i = 1; i < int; i++) {
//       arr.push(`tmp${i}`);
//    };
   
//    console.log(`console.table([${arr.join( ",\n" )}]);`);
// }
//tmpRange(INT);
// _________________________________________________________________________________
function Tmp(Номер, Браузер, Разрешение, Проблема, Описание, Решение) {
  this.N = Номер;
  this.Браузер = Браузер;
  this.Разрешение = Разрешение;
  this.Проблема = Проблема;
  this.Описание = Описание;
  this.Решение = Решение;
}

const INT = 5;
const data = [];

const browsers = ['Chrome', 'Firefox', 'Safari', 'Edge'];
const resolutions = ['320x481', '360x740', '360x740', '320x570'];
const issues = ['carousel', 'предыдущие проблемы', 'предыдущие проблемы', 'section participants'];
const description = ['вёрстка прибита к правому краю', 'уже озвучено', 'уже озвучено', 'вёрстка прибита к левому краю'];
const solution = ['испроавить css код', 'решить вышестоящие проблемы', 'решить вышестоящие проблемы', 'испроавить css код'];

for (let i = 1; i < INT; i++) {
  data.push(
    new Tmp(
      i,
      browsers[i % browsers.length],
      resolutions[i % resolutions.length],
      issues[i % issues.length],
      description[i % description.length],
      solution[i % solution.length],
      `Тестовый кейс для сценария #${i}`
    )
  );
}

console.table(data);
