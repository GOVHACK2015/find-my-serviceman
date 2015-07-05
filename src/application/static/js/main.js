// Initialise Arbor + Settings
//var sys = arbor.ParticleSystem(1000,1000,0.5,true,55,0.02,0.6);
//sys.renderer = Renderer('#viewport');
//sys.screenSize($('#viewport').width()/2,$('#viewport').height()/2);
var sys
function myFunction(data) {

  sys = arbor.ParticleSystem(1000,1000,0.5,true,55,0.02,0.6);
  sys.renderer = Renderer('viewport');
  sys.screenSize($('#viewport').width()/2,$('#viewport').height()/2);
  
  var center_man = data.name;
	console.log(center_man);
  
  var searchedPerson = sys.addNode('searchedPerson', { 'color':'red','label': center_man,'fixed':'true'} );
  
	// for (var i = 0; i < anythings.children.length; i++) {
	// 	var curr_unit = anythings.children[i];
	// 	console.log(curr_unit);
	// 	var unit_number = anythings.children[i].name;
	// 	console.log(unit_number);

	// 	for (var j = 0; j < curr_unit.children.length; j++) {
	// 		var curr_rank = curr_unit.children[j];
	// 		console.log(curr_rank);

	// 		for (var k = 0; k < curr_rank.children.length; k++) {
	// 			var curr_squad_mem = curr_rank.children[k];
	// 			console.log(curr_squad_mem);
	// 		}
	// 	}
	// }
}

// EXAMPLE
// Add the People Data

/*

var aNewGuy = "Josh Gt. Slapped";

var person1 = sys.addNodYe('Person1', {'color':'green','shape':'square','label':aNewGuy,,'x':$('#viewport').width()/2,'y':$('#viewport').height()/2});

var unit1 = sys.addNode('Unit1', {'color':'brown','shape':'dot','label':'22nd Battalion'});
var person2 = sys.addNode('Person2', {'color':'green','shape':'square','label':'James F. Crux'});
var person3 = sys.addNode('Person3', {'color':'green','shape':'square','label':'Tim R. Ollio'});

var unit2 = sys.addNode('Unit2', {'color':'brown','shape':'dot','label':'5th Artillery'});
var person4 = sys.addNode('Person4', {'color':'green','shape':'square','label':'Tim F. Lee'});
var person5 = sys.addNode('Person5', {'color':'green','shape':'square','label':'Alan B. Gawn'});

sys.addEdge(person1,unit1);
sys.addEdge(person1,unit2);

sys.addEdge(unit1,person2);
sys.addEdge(unit1,person3);

sys.addEdge(unit2,person4);
sys.addEdge(unit2,person5);

*/

/*----------------------------------------------------------------*/
/*----------------------------------------------------------------*/
/*----------------------------------------------------------------*/

// A bit of importing
// Central Person

// var searchedPersonData = JSON.parse({{   }});
// var searchedPerson = sys.addNode('searchedPerson', { 'color':'red','label': 'searchedPerson','fixed':'true'} );

