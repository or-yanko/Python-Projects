// api url
const url = "http://universities.hipolabs.com/search?country=Israel";

function getDataFromUrl(url1)
{
    //create XMLHttpRequest object
    var XMLHttpRequest = require('xhr2');
    const xhr = new XMLHttpRequest();
    //open a get request with the remote server URL
    xhr.open("GET", url1);
    //send the Http request
    xhr.send();


    //triggered when the response is completed
    xhr.onload = function() {
        if (xhr.status === 200) {
            //parse JSON datax`x
            data = JSON.parse(xhr.responseText);
            console.log(data);
            return data;
        } 
        else if (xhr.status === 404) {
            return "No records found";
        }
    }
}





console.log(getDataFromUrl(url));


/*var link = "http://universities.hipolabs.com/search?country=Israel";

function parseURLParams(url) {
    var queryStart = url.indexOf("?") + 1,
        queryEnd   = url.indexOf("#") + 1 || url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {}, i, n, v, nv;

    if (query === url || query === "") return;

    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=", 2);
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);

        if (!parms.hasOwnProperty(n)) parms[n] = [];
        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms;
}

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}



data =  httpGet(link);
console.log(data);
 */