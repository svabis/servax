function menesa_dienas(gads, menesis){
		return new Date(gads,menesis+1,0).getDate(); // 0 - limits (max diena)
}
function clears(){
	var garums = document.getElementById("tab_bod").childNodes.length,
		parents = document.getElementById("tab_bod"),
		elementi = parents.getElementsByTagName("tr");
		for(var i=0; i < garums; i++){
			parents.removeChild(parents.firstChild);
		}
}
function men_not(){
	var datums = new Date(),
		tag_gads = datums.getFullYear(),
		tag_menesis = datums.getMonth(),
		tag_diena = datums.getDay(),
		men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay(), // 0 - pirma diena
		next_poga = document.getElementById("next_poga"),
		prev_poga = document.getElementById("prev_poga");
		next_poga.addEventListener("click", function(){
			clears();
			if(tag_menesis < 11){
			tag_menesis += 1;
			}
			else{
				tag_menesis = 0;
				tag_gads = tag_gads + 1;
			}
			men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay();
			cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis), men_pirma_diena);
		});
		prev_poga.addEventListener("click", function(){
			clears();
			if(tag_menesis == 0){
			tag_menesis = 11;
			tag_gads -= 1;
			}
			else{
				tag_menesis -= 1;
			}
			men_pirma_diena = new Date(tag_gads, tag_menesis, 0).getDay();
			cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis), men_pirma_diena);
		});
		cal_izveide(tag_gads, tag_menesis, menesa_dienas(tag_gads,tag_menesis),men_pirma_diena);
}

function cal_izveide(gads, menesis, men_dienas, men_pirma_diena){
	var	title = document.getElementById("title"),
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
		next_poga.addEventListener("mouseover",function(){
			$(this).animate({
				opacity:1,
			},"fast");
		});
		next_poga.addEventListener("mouseout",function(){
			$(this).animate({
				opacity:0.5
			},"fast");
		});
		prev_poga.addEventListener("mouseover",function(){
			$(this).animate({
				opacity:1
			},"fast");
		});
		prev_poga.addEventListener("mouseout",function(){
			$(this).animate({
				opacity:0.5,
			},"fast");
		});
		for(var i=0; i < nedelas; i++){
			rinda = document.createElement("tr");
			tabula.appendChild(rinda);
			rinda.setAttribute("id", i+1 + " Nedela");
			tab_rinda = document.getElementById(i+1 + " Nedela");
			for(var j=0; j < 7; j++){
				elements = document.createElement("td");
				elements.setAttribute("class","text-center");
				if(count == tag_diena && menesis == tag_menesis && tag_gads == gads){
					elements.setAttribute("style","font-size:24px;vertical-align:middle;border:2px solid #4286f4");
				}
				else
				{
					elements.setAttribute("style","font-size:24px;vertical-align:middle;border:1.5px solid #999;height:80px;width:80px");
				}
				if(count <= men_dienas){
					if(men_pirma_diena > j && i == 0){
						txt = document.createTextNode("");
						}
					else{
						txt = document.createTextNode(count);
						count ++;
					}
				}
				else{
					txt = document.createTextNode("");
				}
				tab_rinda.appendChild(elements);
				elements.appendChild(txt);
			}
		};
		eventu_pievienosana(gads, menesis);
}
function eventu_pievienosana(gads, menesis){
	var eventi = notikumi,
		menesis = Number(menesis) + 1,
		kalendars = document.getElementById("kalendars"),
		tabula = document.getElementById("tab_bod"),
		elementi = tabula.getElementsByTagName("td"),
		eventu_datumi, elementa_saturs, events, parents, kamera, eventu_containers,
		modalis, modal_dialog, modal_contents, modal_header,close_poga,title,title_txt,modal_body,v_bloks,video,v_src;
		for(var i=0; i < elementi.length; i++){
			elementa_saturs = tabula.getElementsByTagName("td").item(i).innerHTML;
			if(elementa_saturs.length == 1){
			    elementa_saturs = "0" + elementa_saturs;
			}
			parents = tabula.getElementsByTagName("td").item(i);
			eventu_containers = document.createElement("div");
			eventu_containers.setAttribute("style","padding:0;margin:0");
			for (var j = 0; j < eventi.length; j++){
				eventu_datumi = eventi[j].start.split("-");
				kamera = eventi[j].title;
					if(eventu_datumi[0] == gads && eventu_datumi[1] == menesis && eventu_datumi[2] == elementa_saturs){
						events = document.createElement("span");

						events.addEventListener("mouseover", function(){
							$(this).animate({
								opacity:1,
								fontSize:"+=5px"
							},"fast");
						});
						events.addEventListener("mouseout", function(){
							$(this).animate({
								opacity:0.5,
								fontSize:"-=5px"
							},"fast");
						});
						if(kamera == "Lapenes kamera"){
							modalis = document.createElement("div");
							modal_dialog = document.createElement("div");
							modal_contents = document.createElement("div");
							modal_header = document.createElement("div");
							close_poga = document.createElement("button");
							close_poga_txt = document.createTextNode("&times;");
							title = document.createElement("h4");
							title_txt = document.createTextNode("Video no "+eventi[j].start);
							modal_body = document.createElement("div");
							v_bloks = document.createElement("div");
							video = document.createElement("video");
							v_src = document.createElement("source");
							events.setAttribute("class", "glyphicon glyphicon-facetime-video");
							events.setAttribute("style","float:right;color:#bbb;cursor:pointer;opacity:0.5");
							events.setAttribute("data-toggle","modal");
							events.setAttribute("data-target","#" + j);
							modalis.setAttribute("id",j);
							modalis.setAttribute("class","modal fade");
							modalis.setAttribute("role","dialog");
							modal_dialog.setAttribute("class","modal-dialog modal-md");
							modal_contents.setAttribute("class","modal-content");
							modal_header.setAttribute("class", "modal-header");
							close_poga.setAttribute("class","close");
							close_poga.setAttribute("data-dismiss","modal");
	
//							close_poga.setAttribute("id","video_modal_close");
							close_poga.innerHTML = "&times;";
							title.setAttribute("class","modal-title text-center");
							modal_body.setAttribute("class","modal-body");
							modal_body.setAttribute("style","background-color:#666");
							v_bloks.setAttribute("class","embed-responsive embed-responsive-4by3");
							video.setAttribute("controls","");
							v_src.setAttribute("src", eventi[j].url);
							v_src.setAttribute("type","video/mp4");
							video.appendChild(v_src);
							v_bloks.appendChild(video);
							modal_body.appendChild(v_bloks);
							title.appendChild(title_txt);
							modal_header.appendChild(close_poga);
							modal_header.appendChild(title);
							modal_contents.appendChild(modal_header);
							modal_contents.appendChild(modal_body);
							modal_dialog.appendChild(modal_contents);
							modalis.appendChild(modal_dialog);
							kalendars.appendChild(modalis);
							}
						else if(kamera ==  "Mājas kamera"){
							modalis = document.createElement("div");
							modal_dialog = document.createElement("div");
							modal_contents = document.createElement("div");
							modal_header = document.createElement("div");
							close_poga = document.createElement("button");
							close_poga_txt = document.createTextNode("&times;");
							title = document.createElement("h4");
							title_txt = document.createTextNode("Video no "+eventi[j].start);
							modal_body = document.createElement("div");
							v_bloks = document.createElement("div");
							video = document.createElement("video");
							v_src = document.createElement("source");
							events.setAttribute("class", "text-center glyphicon glyphicon-home");
							events.setAttribute("style","float:left;color:#00c7ff;cursor:pointer;opacity:0.5");
							events.setAttribute("data-toggle","modal");
							events.setAttribute("data-target","#" + j);
							modalis.setAttribute("id",j);
							modalis.setAttribute("class","modal fade");
							modalis.setAttribute("role","dialog");
							modal_dialog.setAttribute("class","modal-dialog modal-md");
							modal_contents.setAttribute("class","modal-content");
							modal_header.setAttribute("class", "modal-header");
							close_poga.setAttribute("class","close");
							close_poga.setAttribute("data-dismiss","modal");
	
//							close_poga.setAttribute("id","video_modal_close");
							close_poga.innerHTML = "&times;";
							title.setAttribute("class","modal-title text-center");
							modal_body.setAttribute("class","modal-body");
							modal_body.setAttribute("style","background-color:#666");
							v_bloks.setAttribute("class","embed-responsive embed-responsive-4by3");
							video.setAttribute("controls","");
							v_src.setAttribute("src", eventi[j].url);
							v_src.setAttribute("type","video/mp4");
							video.appendChild(v_src);
							v_bloks.appendChild(video);
							modal_body.appendChild(v_bloks);
							title.appendChild(title_txt);
							modal_header.appendChild(close_poga);
							modal_header.appendChild(title);
							modal_contents.appendChild(modal_header);
							modal_contents.appendChild(modal_body);
							modal_dialog.appendChild(modal_contents);
							modalis.appendChild(modal_dialog);
							kalendars.appendChild(modalis);
							}
						else if(kamera ==  "Šķūnīša kamera"){
							modalis = document.createElement("div");
							modal_dialog = document.createElement("div");
							modal_contents = document.createElement("div");
							modal_header = document.createElement("div");
							close_poga = document.createElement("button");
							close_poga_txt = document.createTextNode("&times;");
							title = document.createElement("h4");
							title_txt = document.createTextNode("Video no "+eventi[j].start);
							modal_body = document.createElement("div");
							v_bloks = document.createElement("div");
							video = document.createElement("video");
							v_src = document.createElement("source");
							events.setAttribute("class", "text-center glyphicon glyphicon-facetime-video");
							events.setAttribute("style","float:right;color:#bbb;cursor:pointer;opacity:0.5");
							events.setAttribute("data-toggle","modal");
							events.setAttribute("data-target","#" + j);
							modalis.setAttribute("id",j);
							modalis.setAttribute("class","modal fade");
							modalis.setAttribute("role","dialog");
							modal_dialog.setAttribute("class","modal-dialog modal-md");
							modal_contents.setAttribute("class","modal-content");
							modal_header.setAttribute("class", "modal-header");
							close_poga.setAttribute("class","close");
							close_poga.setAttribute("data-dismiss","modal");
	
//							close_poga.setAttribute("id","video_modal_close");
							close_poga.innerHTML = "&times;";
							title.setAttribute("class","modal-title text-center");
							modal_body.setAttribute("class","modal-body");
							modal_body.setAttribute("style","background-color:#666");
							v_bloks.setAttribute("class","embed-responsive embed-responsive-4by3");
							video.setAttribute("controls","");
							v_src.setAttribute("src", eventi[j].url);
							v_src.setAttribute("type","video/mp4");
							video.appendChild(v_src);
							v_bloks.appendChild(video);
							modal_body.appendChild(v_bloks);
							title.appendChild(title_txt);
							modal_header.appendChild(close_poga);
							modal_header.appendChild(title);
							modal_contents.appendChild(modal_header);
							modal_contents.appendChild(modal_body);
							modal_dialog.appendChild(modal_contents);
							modalis.appendChild(modal_dialog);
							kalendars.appendChild(modalis);
							}
						else if(kamera ==  "Vārtu kamera"){
							modalis = document.createElement("div");
							modal_dialog = document.createElement("div");
							modal_contents = document.createElement("div");
							modal_header = document.createElement("div");
							close_poga = document.createElement("button");
							close_poga_txt = document.createTextNode("&times;");
							title = document.createElement("h4");
							title_txt = document.createTextNode("Video no "+eventi[j].start);
							modal_body = document.createElement("div");
							v_bloks = document.createElement("div");
							video = document.createElement("video");
							v_src = document.createElement("source");
							events.setAttribute("class", "text-center glyphicon glyphicon-home");
							events.setAttribute("style","float:left;color:#00c7ff;cursor:pointer;opacity:0.5");
							events.setAttribute("data-toggle","modal");
							events.setAttribute("data-target","#" + j);
							modalis.setAttribute("id",j);
							modalis.setAttribute("class","modal fade");
							modalis.setAttribute("role","dialog");
							modal_dialog.setAttribute("class","modal-dialog modal-md");
							modal_contents.setAttribute("class","modal-content");
							modal_header.setAttribute("class", "modal-header");
							close_poga.setAttribute("class","close");
							close_poga.setAttribute("data-dismiss","modal");
	
//							close_poga.setAttribute("id","video_modal_close");
							close_poga.innerHTML = "&times;";
							title.setAttribute("class","modal-title text-center");
							modal_body.setAttribute("class","modal-body");
							modal_body.setAttribute("style","background-color:#666");
							v_bloks.setAttribute("class","embed-responsive embed-responsive-4by3");
							video.setAttribute("controls","");
							v_src.setAttribute("src", eventi[j].url);
							v_src.setAttribute("type","video/mp4");
							video.appendChild(v_src);
							v_bloks.appendChild(video);
							modal_body.appendChild(v_bloks);
							title.appendChild(title_txt);
							modal_header.appendChild(close_poga);
							modal_header.appendChild(title);
							modal_contents.appendChild(modal_header);
							modal_contents.appendChild(modal_body);
							modal_dialog.appendChild(modal_contents);
							modalis.appendChild(modal_dialog);
							kalendars.appendChild(modalis);
							}
						else{
							alert("Alex's kaut ko sačakarēja");
						}
						eventu_containers.appendChild(events);
						parents.appendChild(eventu_containers);
					}
			}
		}
}
