function menesa_dienas(gads, menesis){
  return new Date(gads,menesis+1,0).getDate(); // 0 - limits (max diena)
}

function clearCalendar(){
  var garums = document.getElementById("tab_bod").childNodes.length,
      parents = document.getElementById("tab_bod"),
      elementi = parents.getElementsByTagName("tr");
  for(var i=0; i < garums; i++){
    parents.removeChild(parents.firstChild);
  }
}

function initCalendar(){
  var datums = new Date(),
      tag_gads = datums.getFullYear(),
      tag_menesis = datums.getMonth(),
      tag_diena = datums.getDay(),
      men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay(), // 0 - pirma diena
      next_poga = document.getElementById("next_poga"),
      prev_poga = document.getElementById("prev_poga");

  next_poga.addEventListener("click", function(){
    clearCalendar();
    if(tag_menesis < 11){ tag_menesis += 1; }
    else{ tag_menesis = 0; tag_gads = tag_gads + 1; }
    men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay();
    cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis), men_pirma_diena);
  });

  prev_poga.addEventListener("click", function(){
    clearCalendar();
    if(tag_menesis == 0){ tag_menesis = 11; tag_gads -= 1; }
    else{ tag_menesis -= 1; }
    men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay();
    cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis), men_pirma_diena);
  });

  cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis),men_pirma_diena);
}

function cal_izveide(gads, menesis, men_dienas, men_pirma_diena){
  var title = document.getElementById("title"),
      tabula = document.getElementById("tab_bod"),
      next_poga = document.getElementById("next_poga"),
      prev_poga = document.getElementById("prev_poga"),
      datums = new Date(),
      nedelas = Math.ceil((men_dienas + men_pirma_diena)/7),
      men_sar = ["Janvāris","Februāris","Marts","Aprīlis","Maijs", "Jūnijs", "Jūlijs", "Augusts","Septembris","Oktobris","Novembris","Decembris"],
      count = 1,
      rinda, elements, txt, tab_rinda, tag_diena, tag_gads, tag_menesis;

  title.innerHTML = gads + " " + men_sar[menesis];
  tag_diena = datums.getDate();
  tag_menesis = datums.getMonth();
  tag_gads = datums.getFullYear();

  next_poga.addEventListener("mouseover",function(){ $(this).animate({ opacity:1 },"fast"); });
  next_poga.addEventListener("mouseout",function(){ $(this).animate({ opacity:0.5 },"fast"); });
  prev_poga.addEventListener("mouseover",function(){ $(this).animate({ opacity:1 },"fast"); });
  prev_poga.addEventListener("mouseout",function(){ $(this).animate({ opacity:0.5 },"fast"); });

  for(var i=0; i < nedelas; i++){
    rinda = document.createElement("tr");
    tabula.appendChild(rinda);
    rinda.setAttribute("id", i+1 + " Nedela");
    tab_rinda = document.getElementById(i+1 + " Nedela");
    for(var j=0; j < 7; j++){
      elements = document.createElement("td");
      elements.setAttribute("class","text-center");

      if(count == tag_diena && menesis == tag_menesis && tag_gads == gads){
        if (j==5 || j==6){
          elements.setAttribute("style","font-size:24px;vertical-align:middle;border:3px solid #4286f4;color:#b50e0e;background-color:#efffc7;");
        } else {
          elements.setAttribute("style","font-size:24px;vertical-align:middle;border:3px solid #4286f4");
        }
      } else {
        if (j==5 || j==6){
          elements.setAttribute("style","font-size:24px;vertical-align:middle;border:1.5px solid #999;height:80px;width:80px;color:#b50e0e;background-color:#efffc7;");
        } else {
          elements.setAttribute("style","font-size:24px;vertical-align:middle;border:1.5px solid #999;height:80px;width:80px");
        }
      }
      // comments
      for(var k=0; k < comments.length; k++){
        cDate = comments[k].date.split("-");
        if(men_pirma_diena > j && i == 0) {} else {
          if(count == cDate[2] && menesis+1 == cDate[1] && gads == cDate[0]){
            elements.style.backgroundColor = "#ac68d4";
            elements.style.border = "1.5px solid #8f30c7";
            elements.setAttribute("title", comments[k].comment);
          }
        }
      }

      if(count <= men_dienas){
        if(men_pirma_diena > j && i == 0){ txt = document.createTextNode(""); } else { txt = document.createTextNode(count); count ++; }
      } else { txt = document.createTextNode(""); }

      tab_rinda.appendChild(elements);
      elements.appendChild(txt);
    }
  };
  eventAdd(gads, menesis);
}

function eventAdd(gads, menesis){
  var eventi = notikumi,
      menesis = Number(menesis) + 1,
      kalendars = document.getElementById("kalendars"),
      tabula = document.getElementById("tab_bod"),
      elementi = tabula.getElementsByTagName("td"),
      eventu_datumi, elementa_saturs, events, parents, eventu_containers;

  for(var i=0; i < elementi.length; i++){
    elementa_saturs = tabula.getElementsByTagName("td").item(i).innerHTML;

    if(elementa_saturs.length == 1){ elementa_saturs = "0" + elementa_saturs; }

    parents = tabula.getElementsByTagName("td").item(i);
    eventu_containers = document.createElement("div");
    eventu_containers.setAttribute("style", "padding:0;margin:0");

    for (var j=0; j < eventi.length; j++){
      eventu_datumi = eventi[j].start.split("-");

      if(eventu_datumi[0] == gads && eventu_datumi[1] == menesis && eventu_datumi[2] == elementa_saturs){
        events = document.createElement("span");

        events.addEventListener("mouseover", function(){ $(this).animate({ opacity:1, fontSize:"+=5px" },"fast"); });
        events.addEventListener("mouseout", function(){ $(this).animate({ opacity:0.6, fontSize:"-=5px" },"fast"); });
        events.addEventListener("click", function(){ showVideo(this); });

     // Get icon, color, title
        var icon, title, color;
        for (var k=0; k < camData.length; k++){
          if (camData[k].id==eventi[j].id){ title = camData[k].name; icon = camData[k].icon; color = camData[k].color; }}

        events.setAttribute("class", "glyphicon glyphicon-"+icon);
        events.setAttribute("style", "float:right; color:"+color+"; cursor:pointer; opacity:0.6; margin-left:2px;");
        events.setAttribute("title", title);
        events.setAttribute("id", eventi[j].url);

        eventu_containers.appendChild(events);
        parents.appendChild(eventu_containers);
      }
    }
  }
}
