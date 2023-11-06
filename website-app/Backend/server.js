const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const mainRouter = require('./Routes/mainRouter')
const schuelerRouter = require("./Routes/schuelerRouter")
const anwesenRouter = require("./Routes/anwesenRouter")
const countRouter = require("./Routes/countRouter")

const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use("/api/main", mainRouter);
app.use("/api/schueler", schuelerRouter)
app.use("/api/anwesenheit", anwesenRouter)
app.use("/api/count", countRouter)
app.listen(4000);

// Designed & Developed with <3 and C@f3 by AliJenesyx