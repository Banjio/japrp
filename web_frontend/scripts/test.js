async function fetchAsync (url) {
    let response = await fetch(url);
    let data = await response.json();
    return data;
  }

  var data = fetchAsync("https://httpbin.org/ip")
  console.log(data);