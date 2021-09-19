var express = require("express");
var app = express();


const { MongoClient, ObjectId } = require("mongodb");
var url = "mongodb://localhost:27017";


app.use(express.urlencoded({ extended: true }))
app.use(express.json());


app.get("/sampleusers", (req, res) => {
    MongoClient.connect(url, (err, conn) => {
        var db = conn.db("delta");
        db.collection("PostMan").find()
            .toArray((err, data) => {
                console.log(data)
                res.send(data);
            })
    })
})
app.post("/addsampleusers", function (req, res) {
    MongoClient.connect(url, function (err, conn) {
        var db = conn.db("delta");
        db.collection("PostMan").insertOne(req.body, function (err, data) {
            res.send(data)
        })
    })
});

app.post("/sampleuser/:id", function (req, res) {
    MongoClient.connect(url, (err, conn) => {
        var db = conn.db("delta")
        db.collection('PostMan').deleteOne({ _id: ObjectId(req.params.id) }, function (err, data) {
            res.send(data)
        })
    })
})


app.patch("/sampleuserupdt/:id", function (req, res) {
    MongoClient.connect(url, function (err, conn) {
        var db = conn.db("delta")
        db.collection("PostMan").updateOne({ _id: ObjectId(req.params.id) }, {
            $set: req.body
        }, function (err, data) {
            res.send(data)
        })
    })
})
app.listen(8080, function () { console.log("Listening on 8080") });