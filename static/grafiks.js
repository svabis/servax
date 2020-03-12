//"use strict";
function dienas(datumsNo, datumsLidz){
	var jaunsDatums = new Date(datumsNo),
		jaunsDatums2 = new Date(datumsLidz),
		parveidotais = jaunsDatums.getTime(),
		parveidotais2 = jaunsDatums2.getTime(),
		x = parveidotais2 - parveidotais,
		dienas = (x/86400000).toFixed(0);
		return Number(dienas);
}//Funkcija, kas aprÄ“Ä·ina cik dienas ir starp sÄkotnÄ“jo datyumu un beigu datumu

var koeficientu_objekts = {platums:0,augstums:0},
	krasu_objekts = {
	graf_bloks:"#000",
	graf_bultas:"#FFF",
	pozitivs:"#ff2626",
	negativs:"#FFF",
	info_box_krasa:"#cc0e0e",
	};

function parlade(datums,paterins){
	var bloks = document.getElementById("Grafiks"),
		apli = document.getElementsByTagName("circle"),
		datumu_masivs = datums;
		paterina_masivs = paterins;
//		var graf_bloks = document.getElementById("pat_graf");
		bloks_parladets = bloks.innerHTML;
		bloks.innerHTML = bloks_parladets;
//		graf_bloks_parladets = graf_bloks.innerHTML;
//		graf_bloks.innerHTML = graf_bloks_parladets;
		for (i = 0; i < apli.length; i++){
			document.getElementsByTagName("circle").item(i).setAttribute("id", i);
			document.getElementsByTagName("circle").item(i).addEventListener(
			"mouseover",function(){
				info_show(
				document.getElementsByTagName("line").item(Number(this.getAttribute("id"))-1),
				document.getElementsByTagName("circle").item(this.getAttribute("id")),
				this.getAttribute("id"),
				this.getAttribute("cx"),
				this.getAttribute("cy"),
				datumu_masivs,
				paterina_masivs)
				});
			document.getElementsByTagName("circle").item(i).addEventListener(
			"mouseout", function(){
				info_hide(
				document.getElementsByTagName("circle").item(this.getAttribute("id")),
				document.getElementsByTagName("line").item(Number(this.getAttribute("id"))-1),
				this.getAttribute("cx"),
			this.getAttribute("cy"),
				this.getAttribute("id"),
				paterina_masivs);
				});
		}
		eventu_funkcija();
}//PÄrlÄdÄ“Å¡anas funkcija, lai HTML bÅ«tu spÄ“jÄ«gs parÄdÄ«t SVG bloku
function info_show(taisne,aplis,id,cx,cy,datums,paterins){
	if(document.getElementById("Bloks" + id) != null){return;};//Lai neisprÅ«stu
	function info_objekts(id){
		this.id = "Bloks" + id;
	}//info objekts
	function close_boxs(src,width,height){
		this.src = src;
		this.width = width;
		this.height = height
	}
	var bloks = document.createElement("div"),
	close_bloks = document.createElement("div"),
	owners = document.getElementById("Grafiks"),
	starpiba = (paterins[id] - paterins[id-1]),
	iznakums = isNaN(starpiba) ? 0 : starpiba,
	close_bloka_elements,
	info_bloks,
	info_virsraksts,
	info_teksts,
	info_teksts2,
	check = (paterins[id] < paterins[id-1]),
	rezultats = check ? "": "+",
	bloka_virsraksts = document.createElement("h1"),
	bloka_elements = document.createElement("p"),
	bloka_elements2 = document.createElement("p"),
	bloka_virsraksta_teksts = document.createTextNode("Datums: " + datums[id]),
	bloka_elementa_teksts = document.createTextNode("Patēriņš: " + paterins[id]),
	bloka_elementa_teksts2 = document.createTextNode("Kopš iepriekšējā: " + rezultats + iznakums),
	tops = Number(cy) - 60,
	lefts = 47 + Number(cx),
	bloka_objekts = new info_objekts(id);//Bloka ID
	bloks.setAttribute("id",bloka_objekts.id);
	close_bloks.setAttribute("id",bloka_objekts.id + "close");
	bloka_virsraksts.setAttribute("id",bloka_objekts.id + "virsraksts");
	bloka_elements.setAttribute("id",bloka_objekts.id + "pirmais");
	bloka_elements2.setAttribute("id",bloka_objekts.id + "otrais");
	$(aplis).animate({"r":10},125,function(){
		$(this).css("fill",
		check ? "#ff3232" : "#00e5ff"
		);
	});
	if(taisne != null){
		$(taisne).animate({"stroke-width":"4px"},125,function(){
				$(this).css("stroke",
				check ? "#ff3232" : "#00e5ff"
				);
			});
	}
	$(bloka_virsraksts).append(bloka_virsraksta_teksts);
	$(bloka_elements).append(bloka_elementa_teksts);
	$(bloka_elements2).append(bloka_elementa_teksts2);
	$(bloks).append(close_bloks).append(bloka_virsraksts).append(bloka_elements).append(bloka_elements2);
	$(owners).append(bloks);
	info_bloks = document.getElementById(bloka_objekts.id);
	close_bloka_elements = document.getElementById(bloka_objekts.id + "close");
	info_virsraksts = document.getElementById(bloka_objekts.id + "virsraksts");
	info_teksts = document.getElementById(bloka_objekts.id + "pirmais");
	info_teksts2 = document.getElementById(bloka_objekts.id + "otrais");
	$(info_bloks).css({
		"position":"absolute",
		"display":"block",//none defaults
		"top": Number(cy) + 43 + "px",
		"left": Number(cx) + 47 + "px",
		"height":"0px",
		"background-color":"#FFF",
		"border":"2px outset",
		"border-color":
		check ? "#ff3232" : "#00e5ff",
		"border-radius":"3px",
		"z-index":9999,
		"opacity":0
	});//KlÄt fadeIn() ja kas nesanÄk ar animate
	$(info_bloks).animate({
		"left":lefts-80 + "px",
		"top":tops + "px",
		"min-width":"140px",
		"padding":"0.5%",
		"margin":"0.5%",
		"height":"13%",
		"display":"flex",
		"opacity":1
		},250);
	$(close_bloka_elements).css({
		"position":"relative",
		"width":"15%",
		"height":"20px",
		"float":"right",
		"background-image":"url( 'http://svabwilla.svabis.eu/static/graf_close.png' )",
		"background-size":"contain",
		"background-repeat":"no-repeat",
		"background-position":"static",
		"cursor":"pointer"
		});
	$(info_virsraksts).css({
		"text-align":"left",
		"font-size":"0.8em",
		});
	$(info_teksts).css({
		"font-size":"0.8em",
		});
	$(info_teksts2).css({
		"font-size":"0.8em",
		});
	close_bloka_elements.addEventListener("click", function(){
		$(info_bloks).animate({
		"left": Number(cx) + 47 + "px",
		"top": Number(cy) + 43 + "px",
		"width":"0px",
		"height":"0px",
		"opacity":0
		},250,function(){;
			$(aplis).animate({"r":5},125,function(){
				$(this).css("fill",
				check ? "#af0000" : "#080082"
				);
			});
			$(taisne).animate({"stroke-width":"2px"},125,function(){
				$(this).css("stroke",
				check ? "#ff0000" : "#0186ba"
				);
			});
			$(info_bloks).remove();
		});
	});
}
function info_hide(aplis,taisne,cx,cy,id,paterins){
	//if(info_show(parbaude) == true){return;};//Lai neisprÅ«stu
	var owners = document.getElementById("Grafiks"),
		childs = document.getElementById("Bloks" + id),
		intervals,
		check = (paterins[id] < paterins[id-1]),
		timeouts,
		opacitys = 1;
		if(childs.style.opacity  < 1){return;};
		intervals = setInterval(function(){
			$(childs).css("opacity",opacitys = opacitys - 0.02);
			},100);
		timeouts = setTimeout(function(){
			$(childs).animate({
				"left": Number(cx) + 47 + "px",
				"top": Number(cy) + 43 + "px",
				"width":"0px",
				"height":"0px",
				"opacity":0
		},250,
			function(){;
				$(aplis).animate({"r":5},125,function(){
					$(this).css("fill",
					check ? "#af0000" : "#080082"
					);
				});
				$(taisne).animate({"stroke-width":"2px"},125,function(){
					$(this).css("stroke",
					check ? "#ff0000" : "#0186ba"
					);
				});
				$(childs).remove();
		});
			},5000);
		childs.addEventListener("mouseenter",function(){
			$(childs).css("opacity",1);
			clearInterval(intervals);
			clearTimeout(timeouts);
		});
		childs.addEventListener("mouseleave",function(){
			var opacitys,countdowns,divs;
			divs = this;
			opacitys = 1,
			countdowns = 50;
			intervals = setInterval(function(){
				countdowns--;
				if(countdowns == 0){
					clearInterval(intervals);
					$(aplis).animate({"r":5},125,function(){
						$(this).css("fill",
						check ? "#af0000" : "#080082"
						);
					});
					$(taisne).animate({"stroke-width":"2px"},125,function(){
						$(this).css("stroke",
						check ? "#ff0000" : "#0186ba"
						);
					});
					$(childs).remove();
				}
				$(childs).css("opacity" ,opacitys = opacitys - 0.02);
			},100);
		});
}
function taisne(x1,y1,x2,y2,stroke_color,stroke_width) {//Lai izveidotu objektu, tiek padotas vÄ“rtÄ«bas
	//PÄri Ä«paÅ¡Ä«basNosaukums = vÄ“rtÄ«ba
	this.x1 = x1;
	this.y1 = y1;
	this.x2 = x2;
	this.y2 = y2;
	this.style = "stroke:" + stroke_color + ";stroke-width:" + stroke_width;
}//Konstruktors taisnes objektam
function palig_taisne(x1,y1,x2,y2, krasa, platums){
	this.d = "M " + x1 + " " + y1 + " L " + x2 + " " + y2;
	this.stroke = krasa;
	this.width = platums;
	}
function plakne(id,platums,augstums){
	//PÄri Ä«paÅ¡Ä«basNosaukums = vÄ“rtÄ«ba
	this.id = id;
	this.width = platums;
	this.height = augstums;
}//SVG elementa objekta konstruktors
function aplis(cx,cy,radius,krasa){
	//PÄri Ä«paÅ¡Ä«basNosaukums = vÄ“rtÄ«ba
	this.cx = cx;
	this.cy = cy;
	this.r = radius;
	this.fill = krasa;
}//ApÄ¼a objekts
function teksts(x,y,krasa,gradi){//x,y atranÄs vietas
	this.x = x;
	this.y = y;
	this.fill = krasa;
	this.transform = "rotate(" + gradi + " " + x + "," + y + ")";// x un y lai zinÄtu kur tekstam jÄbÅ«t pÄ“c rotÄciojas
}//Teksta objekts
function grafiks(ajax_objekts){//GalvenÄ funkcija, kur notiek visa "zÄ«mÄ“Å¡anÄs"/Tiek padots ajax_objekts
	var datu_objekts = JSON.parse(ajax_objekts),//Ajax atbildi(kas tiek padots funkcijai) pÄrveido par JS objektu
		grafika_bloks = document.getElementById("Grafiks"),//mainÄ«gais, kurÅ¡ norÄda uz grafika id
		svg = new plakne("pat_graf", 1200, 400),//JÄiegÅ«st no rÄdijumiem, cik grafikam jÄbÅ«t augstam/platam, izveido objektu no kura tiek uzzÄ«mÄ“ts SVG elements
		datumu_masivs = [],//TopoÅ¡ais datumu masÄ«ovs kurÅ¡ glabÄs visus datumus
		paterina_masivs = [],//TopoÅ¡ais patÄ“riÅ†u masÄ«vs kurÅ¡ glabÄs visus patÄ“riÅ†us
		svg_taisne = "",//TopoÅ¡ais taisnes objekts
		svg_palig_taisne = "",
		svg_plaknes_xass = "",
		svg_plaknes_yass = "",
		kopejas_dienas = 0,
		svg_aplis = "",//TopoÅ¡ais apÄ¼a objekts
		svg_teksts = "",//TopoÅ¡ais teksta objekts
		plaknes_bloks = "",//TopoÅ¡ais DIV ar id pat_graf
		plaknes_taisne= "",//VÄ“lÄk glabÄs izveidotu taisni <line> elementu
		plaknes_aplis = "",//vÄ“lÄk glabÄs izveidotu aplis <circle> elementu
		plaknes_path = "",
		plaknes_xass = "",
		plaknes_yass = "",
		plaknes_teksts = "",//VÄ“lÄk glabÄs izveidoto text elementu
		plaknes_teksts_teksts = "",//VÄ“lÄk glabÄs izveidota teksta mezgla infu(tekstu ko rakstÄ«t plaknes_teksts elementÄ)
		koeficients_augstumam = 0,
		videjais_paterins = 0,
		visas_dienas = 0,
		pirma_diena = 0,
		pedeja_diena = 0,
		diena = "",
		iterators = 0,
		parveidota_diena = 0,
		koeficients_platumam = 0,
		//iterators = 0,
		count1 = 0,//PatreizÄ“jÄis datums/rÄdÄ«jums
		count2 = 1,//NÄkamais datums/rÄdÄ«jums
		//Counteri, ar kuriem lÄ“kÄt pa masÄ«viem
		iepriekseja_diena,//IepriekÅ¡Ä“jÄs dienas vÄ“rtÄ«ba, lai zinÄtu nÄkamajiem x1 zinÄtu iepriekÅ¡Ä“jo x2
		svg_elements = document.createElement("svg");//Izveido jaunu SVG elementu// MainÄ«gie
	for (var x in svg){//Cikls, kurÅ¡ nostrÄdÄ tik daudz reizes, cik ir Ä«paÅ¡Ä«bas objektÄ plakne
		svg_elements.setAttribute(x, svg[x]);
	}//SVG elementam noseto attribÅ«tus
	svg_plaknes_xass = new palig_taisne(0,svg.height-10,svg.width,svg.height-10,"#000",2);
	svg_plaknes_yass = new palig_taisne(0,10,0,svg.height-10,"#000",2);
	plaknes_xass = document.createElement("path");
	plaknes_yass = document.createElement("path");
	for(xass in svg_plaknes_xass){
		plaknes_xass.setAttribute(xass, svg_plaknes_xass[xass]);
	}
	for(yass in svg_plaknes_yass){
		plaknes_yass.setAttribute(yass, svg_plaknes_yass[yass]);
	}
	for (i in datu_objekts.Radijumi){//Cikls kurÅ¡ nostrÄdÄ tik daudz reizes, cik elementi ir objekta masÄ«vÄ
		datumu_masivs.push(datu_objekts.Radijumi[i].Datums);//Aizpilda datumu masÄ«vu ar katra objekta datumu
		paterina_masivs.push(datu_objekts.Radijumi[i].Paterins)//Aizpilda paterina masÄ«vu ar katra objekta patÄ“riÅ†u
	}//MasÄ«vu aizpilde
	grafika_bloks.appendChild(svg_elements);//Pievieno Grafika blokam jauno SVG elementu
	plaknes_bloks = document.getElementById("pat_graf");//Atrod SVG elementu
	pirma_diena = datumu_masivs[0];
	pedeja_diena = datumu_masivs[datumu_masivs.length - 1];
	visas_dienas = dienas(pirma_diena,pedeja_diena);
	if(visas_dienas < 356){
		koeficients_platumam = 2;
	}
	else if(visas_dienas > 356 && visas_dienas < 712){
		koeficients_platumam = 4;
	}
	else{
		koeficients_platumam = 6;
	}//Koeficients platumam
	koeficientu_objekts.platums = koeficients_platumam;
	for(n = 0; n < paterina_masivs.length; n++){
		videjais_paterins += paterina_masivs[n]/paterina_masivs.length;
		if(n == paterina_masivs.length - 1){
			if( videjais_paterins > 400 && videjais_paterins < 800){
				koeficients_augstumam = 1;
			}
			else if(videjais_paterins > 800){
				iterators = 3;//TreÅ¡ais ifs, tÄpÄ“c treÅ¡Ä iterÄcija
				while(videjais_paterins > 800){
					videjais_paterins = Number(videjais_paterins)-400;
					//Izdala ar 2 un iterators par 4 lielÄks
					//Iterators par 4 lielÄks, jo galvenais ir dabÅ«t visas taisnes * 0.5
					// Dalot vidÄ“jo ar 2(0.5+0.5+0.5+0.5) iterators ir 4
					iterators += 1;
					koeficients_augstumam = 1 / iterators;
				}
			}
			else{
				koeficients_augstumam = 2;
			}
		}
	}//Koeficients augstumam
	koeficientu_objekts.augstums = koeficients_augstumam;
	for (y in datu_objekts.Radijumi){//Cikls kurÅ¡ nostrÄdÄ tik reizes, cik ir elementi objekta masÄ«vÄ
	//VarbÅ«t apvienot ar augstÄko ciklu???
		if(count1 == 0){//PirmÄ iterÄcija
			svg_taisne = new taisne//Izveido taisnes objektu ar vÄ“rtÄ«bÄm
			(0,//x1 vÄ“rtÄ«ba
			svg.height-10,//y1 vÄ“rtÄ«ba/sÄkums no lejas - 5, lai smuki datums parÄdÄ«tos
			dienas(datumu_masivs[count1],datumu_masivs[count2])*koeficients_platumam,//x2 vÄ“rtÄ«ba
			//AprÄ“Ä·inÄtais skaitlis ko atgrieÅ¾ dienas funkcija
			svg.height-((paterina_masivs[count2])*koeficients_augstumam),
			//y2 vÄ“rtÄ«ba - pirmais patÄ“riÅ†Å¡ atÅ†emts no svg elementa augstuma, lai sÄktos no apakÅ¡as
			(paterina_masivs[count1] > paterina_masivs[count1+1]) ? "#ff0000":"#0186ba",
			2);//Stils lÄ«nijai//Taisnes objekta izveide
			svg_aplis = new aplis //Izveido apÄ¼a objektu ar vÄ“rtÄ«bÄm
			(svg_taisne.x1,//cx vÄ“rtÄ«ba<line> x1 vÄ“rtÄ«ba, vienmÄ“r
			svg_taisne.y1,//cy vÄ“rtÄ«ba - vienmÄ“r <line> y1 vÄ“rtÄ«ba
			5,
			(paterina_masivs[count1] < paterina_masivs[count1-1]) ? "#af0000":"#080082"
			);//Defaultie stili//Apla objekta izveide
			svg_teksts = new teksts//Izveido teksta objektu
			((svg_aplis.cx-3) - (svg_aplis.r/2),
			//Teksta atraÅ¡anÄs uz x asi - apla radiuss, lai butu precizi uz punkta teksts
			svg.height,
			//Teksta y pozÄ«cija, svg augstums
			"#000",//Teksta krÄsa
			45//RotÄcija grÄdos
			);//Teksta rotÄcija//Teksta objekta izveide
			svg_palig_taisne = new palig_taisne
			(svg_taisne.x1,
			svg_taisne.y1,
			svg_teksts.x + 5.5,
			svg_teksts.y-10,
			"#c4c2c2",
			2);
			iepriekseja_diena = svg_taisne.x2/koeficients_platumam;
			//iepriekseja_diena mainÄ«gais tagad glabÄ x2 skaitli(nÄkamai iterÄcijai - x1)
		}
		else if(count1 == paterina_masivs.length - 1){//PÄ“dÄ“jai iterÄcijai
			svg_taisne = new taisne
			(iepriekseja_diena*koeficients_platumam,
			svg.height-(paterina_masivs[count1]*koeficients_augstumam),
			(iepriekseja_diena*koeficients_platumam)+40,
			svg.height-(paterina_masivs[count1]*koeficients_augstumam),
			(paterina_masivs[count1] > paterina_masivs[count1+1]) ? "#ff0000":"#000",
			2);
			svg_aplis = new aplis
			(svg_taisne.x1,//cx vÄ“rtÄ«ba<line> x1 vÄ“rtÄ«ba, vienmÄ“r
			svg_taisne.y1,//cy vÄ“rtÄ«ba - vienmÄ“r <line> y1 vÄ“rtÄ«ba
			5,
			(paterina_masivs[count1] < paterina_masivs[count1-1]) ? "#af0000":"#080082"
			);//Defaultie stili
			svg_teksts = new teksts//Izveido teksta objektu
			((svg_aplis.cx-3) - (svg_aplis.r/2),
			//Teksta x pozÄ«cija, vienmÄ“r <line> x2 vÄ“rtÄ«ba vai apla cx vÄ“rtÄ«ba - apla radius/2
			svg.height,
			"#000",//Teksta krÄsa
			45);//Teksta rotÄcija
			svg_palig_taisne = new palig_taisne
			(svg_taisne.x1,
			svg_taisne.y1,
			svg_teksts.x + 6,
			svg_teksts.y-10,
			"#c4c2c2",
			2);
		}
		else{//OtrÄ iterÄcija sÄkÄs
			svg_taisne = new taisne
			(iepriekseja_diena*koeficients_platumam,//PaÅ†em pirmajÄ iterÄcijÄ iegÅ«to x2 un ieliek x1 vÄ“rtÄ«bÄ
			svg.height-(paterina_masivs[count1]*koeficients_augstumam),
			//y1 vÄ“rtÄ«ba, sÄkums taisnei(iepriekÅ¡Ä“jÄs iterÄcijas y2 vÄ“rtÄ«ba) ko atnjem no svg augstuma, lai apakÅ¡Ä sÄktos
			(dienas(datumu_masivs[count1],datumu_masivs[count2]) + iepriekseja_diena) *koeficients_platumam,
			//Jaunais x2 bÅ«s dienas cik pagÄjuÅ¡as kopÅ¡ iepriekÅ¡Ä“jÄ rÄdÄ«juma + iepriekÅ¡Ä“jÄd diena, lai x2 pieaugtu(labÄk *2)
			svg.height-(paterina_masivs[count2]*koeficients_augstumam),
			//NÄkamais patÄ“riÅ†Å¡ atÅ†emts no svg augstuma, lai sÄktos no apakÅ¡as
			(paterina_masivs[count1] > paterina_masivs[count1+1]) ? "#ff0000":"#0186ba",
			2);
			svg_aplis = new aplis//Jauns aplis(objekts)
			(svg_taisne.x1,//cx vÄ“rtÄ«ba, vienmÄ“r<line> x1 vÄ“rtÄ«ba
			svg_taisne.y1,//cy vÄ“rtÄ«ba, vienmÄ“r <line> y1 vÄ“rtÄ«ba
			5,
			(paterina_masivs[count1] < paterina_masivs[count1-1]) ? "#af0000":"#080082"
			);
			svg_teksts = new teksts//Izveido teksta objektu
			((svg_aplis.cx-3) - (svg_aplis.r/2),
			//Teksta x pozÄ«cija, vienmÄ“r <line> x2 vÄ“rtÄ«ba vai apla cx vÄ“rtÄ«ba
			svg.height,
			//Teksta y pozÄ«cija, vienmÄ“r svg augstums - 43
			"#000",//Teksta krÄsa
			45);//Teksta rotÄcija
			svg_palig_taisne = new palig_taisne
			(svg_taisne.x1,
			svg_taisne.y1,
			svg_teksts.x + 6,
			svg_teksts.y-10,
			"#c4c2c2",
			2);
			iepriekseja_diena = svg_taisne.x2/koeficients_platumam;
			//MainÄ«gajÄ glabÄjÄs jaunais x1 nÄkamajai iterÄcijai
		}
		plaknes_taisne = document.createElement("line");//PÄ“c ifiem un elsiem izveido jaunu elementu
		plaknes_aplis = document.createElement("circle");//PÄ“c ifiem un elsiem izveido jaunu elementu
		plaknes_teksts = document.createElement("text");//PÄ“c ifiem un elsiem izveidot text elementu
		plaknes_path = document.createElement("path");
		plaknes_teksts_teksts = document.createTextNode(datumu_masivs[count1]);//Izveido teksta mezglu
		plaknes_teksts.appendChild(plaknes_teksts_teksts);//Ieliek plaknes_teksta mezglÄ texta mezglu
		for (z in svg_taisne){//Cikls, kurÅ¡ nostrÄdÄ tik reizes, cik objektam ir Ä«paÅ¡Ä«bas
			plaknes_taisne.setAttribute(z, svg_taisne[z]);//Katru Ä«paÅ¡Ä«bu ar vÄ“rtÄ«bu iemet atrtribÅ«tÄ
		}
		plaknes_bloks.appendChild(plaknes_teksts);//Pieliek text elementu plaknei
		for (u in svg_palig_taisne){
			plaknes_path.setAttribute(u, svg_palig_taisne[u]);
		}
		plaknes_bloks.appendChild(plaknes_path);
		plaknes_bloks.appendChild(plaknes_xass);
		plaknes_bloks.appendChild(plaknes_yass);
		plaknes_bloks.appendChild(plaknes_taisne);//Pievieno izveidoto <line> svg blokam
		for (i in svg_aplis){//Cikls kurÅ¡ nostrÄdÄ tik daudz reizes, cik apÄ¼a objektam bÅ«s Ä«paÅ¡Ä«bas
			plaknes_aplis.setAttribute(i, svg_aplis[i]);//Katru Ä«paÅ¡Ä«bu ar vÄ“rtÄ«bu iemet atrtribÅ«tÄ
		}
		if (count1 != paterina_masivs.length){
			plaknes_bloks.appendChild(plaknes_aplis);//Pievieno apli plaknei
		}
		for (j in svg_teksts){
			plaknes_teksts.setAttribute(j, svg_teksts[j]);//Saliek <text> atribÅ«tus
		}
		//Palielina kounterus, lai varÄ“tu iegÅ«t pareizus x1,y1,y2 un x2 no masÄ«viem
		count1 += 1;
		count2 += 1;
	}//Main cikls ar visiem ifiem
	parlade(datumu_masivs,paterina_masivs);//Izsauc pÄrlÄdÄ“Å¡anas funkciju
}//Grafika funkcija
function eventu_funkcija(){
	var svg = document.getElementsByTagName("svg").item(0),
	rights = document.getElementById("labais"),
	lefts = document.getElementById("kreisais"),
	intervals,
	intervals_back;
rights.addEventListener("touchstart",function(){
	clearInterval(intervals_back);
	intervals = setInterval(right,1);
	});
rights.addEventListener("touchend",function(){
	clearInterval(intervals);
});
lefts.addEventListener("touchstart",function(){
	clearInterval(intervals);
	intervals_back = setInterval(left,1);
});
lefts.addEventListener("touchend",function(){
	clearInterval(intervals_back);
});
rights.addEventListener("mousedown",function(){
	clearInterval(intervals_back);
	intervals = setInterval(right,1);
});
rights.addEventListener("mouseup",function(){
	clearInterval(intervals);
});
rights.addEventListener("mouseleave",function(){
	clearInterval(intervals);
});
lefts.addEventListener("mousedown",function(){
	clearInterval(intervals);
	intervals_back = setInterval(left,1);
});
lefts.addEventListener("mouseup",function(){
	clearInterval(intervals_back);
});
lefts.addEventListener("mouseleave",function(){
	clearInterval(intervals_back);
});
}
function right(){
	var tag_x1, tag_y1, tag_x2, tag_y2, aplis_cx, aplis_cy, teksta_x, teksta_y,aplis_pedejais,svg_augstums2,pirmais_aplis_cx,
	platums = koeficientu_objekts.platums,
	augstums = koeficientu_objekts.augstums,
	bloks = document.getElementById("Grafiks"),
	svg = document.getElementsByTagName("svg").item(0),
	svg_platums = Number(svg.getAttribute("width"))/platums-40,
	taisnes = document.getElementsByTagName("line"),
	pathi = document.getElementsByTagName("path"),
	apli = document.getElementsByTagName("circle"),
	teksti = document.getElementsByTagName("text");
	x_ass = pathi.item(pathi.length-1);
	y_ass = pathi.item(pathi.length-2);
	aplis_pedejais = Number(apli.item(apli.length-1).getAttribute("cx"));
	pirmais_aplis_cx = apli.item(0).getAttribute("cx");
	if(aplis_pedejais - 600 > svg_platums){
		for (k = 0; k < pathi.length-2; k++){
			tag_x1 = Number(taisnes.item(k).getAttribute("x1"));
			tag_y1 = Number(taisnes.item(k).getAttribute("y1"));
			tag_x2 = Number(taisnes.item(k).getAttribute("x2"));
			tag_y2 = Number(taisnes.item(k).getAttribute("y2"));
			taisnes.item(k).setAttribute("x1", tag_x1 - platums);
			taisnes.item(k).setAttribute("y1", tag_y1 + augstums);
			taisnes.item(k).setAttribute("x2", tag_x2 - platums);
			taisnes.item(k).setAttribute("y2", tag_y2 + augstums);
			aplis_cx = Number(apli.item(k).getAttribute("cx"));
			aplis_cy = Number(apli.item(k).getAttribute("cy"));
			apli.item(k).setAttribute("cx", aplis_cx - platums);
			apli.item(k).setAttribute("cy", aplis_cy + augstums);
			teksta_x = Number(teksti.item(k).getAttribute("x"));
			teksta_y = Number(teksti.item(k).getAttribute("y"));
			teksti.item(k).setAttribute("y",teksta_y + (0.71*platums));//MaÄ£iskais 0.7125
			teksti.item(k).setAttribute("x",teksta_x - (0.71*platums));
			pathi.item(k).setAttribute("d", "M " + (Number(aplis_cx) - platums) + " " + (Number(aplis_cy) + augstums) + " L " + (Number(aplis_cx) - platums) + " " + (Number(390)));
			x_ass.setAttribute("d",	"M " + (Number(pirmais_aplis_cx) - platums) + " " + (Number(0))	+ " L " + (Number(pirmais_aplis_cx) - platums) + " " + (Number(390)));
			y_ass.setAttribute("d",	"M " + (Number(pirmais_aplis_cx) - platums) + " " + (Number(390)) + " L " + (Number(1200)) + " " + (Number(390)));
		}
	}
}
function left(){
	var tag_x1, tag_y1, tag_x2, tag_y2, aplis_cx, check = 0,pirmais, aplis_cy, teksta_x, teksta_y, taisnes_x2,	pirmais_aplis_cx,
	platums = koeficientu_objekts.platums,
	augstums = koeficientu_objekts.augstums,
	bloks = document.getElementById("Grafiks"), 
	svg = document.getElementsByTagName("svg").item(0),
	taisnes = document.getElementsByTagName("line"),
	pathi = document.getElementsByTagName("path"),
	apli = document.getElementsByTagName("circle"),
	teksti = document.getElementsByTagName("text");
	pirmais = Number(taisnes.item(0).getAttribute("x1"));
	pirmais_aplis_cx = apli.item(0).getAttribute("cx");
	if(pirmais < check ){
		for(k = 0; k < pathi.length-2; k++){
				//if(pirmais >= 0 ){return;}
				tag_x1 = Number(taisnes.item(k).getAttribute("x1"));
				tag_y1 = Number(taisnes.item(k).getAttribute("y1"));
				tag_x2 = Number(taisnes.item(k).getAttribute("x2"));
				tag_y2 = Number(taisnes.item(k).getAttribute("y2"));
				taisnes.item(k).setAttribute("x1", tag_x1 + platums);
				taisnes.item(k).setAttribute("y1", tag_y1 - augstums);
				taisnes.item(k).setAttribute("x2", tag_x2 + platums);
				taisnes.item(k).setAttribute("y2", tag_y2 - augstums);
				aplis_cx = Number(apli.item(k).getAttribute("cx"));
				aplis_cy = Number(apli.item(k).getAttribute("cy"));
				apli.item(k).setAttribute("cx", aplis_cx + platums);
				apli.item(k).setAttribute("cy", aplis_cy - augstums);
				teksta_x = Number(teksti.item(k).getAttribute("x"));
				teksta_y = Number(teksti.item(k).getAttribute("y"));
				teksti.item(k).setAttribute("y",teksta_y - (0.71*platums));
				teksti.item(k).setAttribute("x",teksta_x + (0.71*platums));
				pathi.item(k).setAttribute("d",
							"M " + 
							(Number(aplis_cx) + platums)
				 			+ " " + 
							(Number(aplis_cy) - augstums)
							+ " L " +
							(Number(aplis_cx) + platums)
							+ " " +
							(Number(390))
			);
			x_ass.setAttribute("d",
			"M " + 
						(Number(pirmais_aplis_cx) + platums)
			 			+ " " + 
						(Number(0))
						+ " L " +
						(Number(pirmais_aplis_cx) + platums)
						+ " " +
						(Number(390))
			);
			y_ass.setAttribute("d",
			"M " + 
						(Number(pirmais_aplis_cx) + platums)
			 			+ " " + 
						(Number(390))
						+ " L " +
						(Number(1200))
						+ " " +
						(Number(390))
			);
		}
	}
}
