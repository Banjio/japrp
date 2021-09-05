import { RadioBrowserApi, StationSearchType } from 'radio-browser-api';

const api = new RadioBrowserApi('My Radio App')

const stations = await api.getStationsBy(StationSearchType.byTag, 'jazz')

console.log(stations)


function search_station(){
  var user_input_station = $("#search-field").text();
  
  console.log(user_input_station);
}
console.log(info)