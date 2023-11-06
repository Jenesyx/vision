const mySql = require("mysql");

const anwesenheit = mySql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "anwesenheit2",
});

module.exports = anwesenheit;


// Designed & Developed with <3 and C@f3 by AliJenesyx