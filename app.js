var express = require('express');
var path = require('path');
var logger = require('morgan');
var bodyParser = require('body-parser');
var neo4j = require('neo4j-driver').v1;
var Static = require('node-static');


var app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');


app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));
app.use(express.static(path.join(__dirname, 'public')));

var driver = neo4j.driver('bolt://localhost', neo4j.auth.basic('neo4j', 'pokemon'));
var session = driver.session();

app.get('/', function(req, res){
    return res.render('start');    
});

app.post('/path/add', function(req, res){
    var pA = req.body.pointA;
    var pB = req.body.pointB;
    console.log(pA);
    return res.render('view', {pointA: pA, pointB:pB,complexity: 1});   
    
     res.redirect('/');
})

app.post('/coord/add', function(req, res){
    var idStr = req.body.coord_id;
    var xStr = req.body.coord_x;
    var yStr = req.body.coord_y;
    var strStr = req.body.coord_str;
    var A=req.body.pA; 
    var B=req.body.pB; 

    var arrId = idStr.split(' ');
    var arrX = xStr.split(' ');
    var arrY = yStr.split(' ');
    var arrStr = strStr.split(' , ');
    var compl = (arrId.length);

    function newDot(id, x, y, str){
        session
        .run(
            'CREATE (a:Dot {id: {idParam}, x: {xParam}, y: {yParam}, str:{strParam} }) RETURN a', 
            {idParam:id, xParam: x, yParam:y, strParam: str})
        .then(function(result){
            result.records.forEach(function(record){
                console.log(record._fields[0].properties);
            })
             //return res.render('view');
        })
        .catch(function(err){
            console.log(err);
        });  
    } 

    for (var i=0; i<arrId.length-1; i++)
    {
        newDot(arrId[i], arrX[i], arrY[i], arrStr[i]);  
    }
    function getCompl(count){
        return (count);
    };
    return res.render('view', {pointA: A, pointB: B, complexity: compl});
    console.log(getCompl(arrId.length));
    
    
     res.redirect('/');
})

app.listen(3000);
console.log('Server Started on Port 3000');

module.exports = app;
