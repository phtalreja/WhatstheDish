$( function() {
    var availableTags = [
      "Corn",
      "Beef",
      "Chicken",
      "Mutton",
      "Pork",
      "Lamb",
      "Gelatin",
      "Sunflower",
      "Poppy",
      "Coriander",
      "Garlic",
      "Mustard",
      "Apple",
      "Carrot",
      "Peach",
      "Plum",
      "Tomato",
      "Banana",
    ];
    $( "#tags" ).autocomplete({
      source: availableTags
    });
  } );
