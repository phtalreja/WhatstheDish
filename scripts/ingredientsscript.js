$( function() {
    var availableTags = [
      'Alfalfa Sprouts', 'Apple', 'Apricot', 'Artichoke', 'Asian Pear', 'Asparagus', 'Atemoya', 'Avocado', 'Bamboo Shoots', 'Banana', 'Bean Sprouts', 'Beans', 'Beets', 'Belgian Endive', 'Bell Peppers', 'Bitter Melon', 'Blackberries', 'Blueberries', 'Bok Choy', 'Boniato', 'Boysenberries', 'Broccoflower', 'Broccoli', 'Brussels Sprouts', 'Cabbage', 'Cactus Pear', 'Cantaloupe', 'Carambola', 'Carrots', 'Casaba Melon', 'Cauliflower', 'Celery', 'Chayote', 'Cherimoya', 'Cherries', 'Coconuts', 'Collard Greens', 'Corn', 'Cranberries', 'Cucumber', 'Dates', 'Dried Plums', 'Eggplant', 'Endive', 'Escarole', 'Feijoa', 'Fennel', 'Figs', 'Garlic', 'Gooseberries', 'Grapefruit', 'Grapes', 'Green Beans', 'Green Onions', 'Greens', 'Guava', 'Hominy', 'Honeydew Melon', 'Horned Melon', 'Iceberg Lettuce', 'Jerusalem Artichoke', 'Jicama', 'Kale', 'Kiwifruit', 'Kohlrabi', 'Kumquat', 'Leeks', 'Lemons', 'Lettuce', 'Lima Beans', 'Limes', 'Longan', 'Loquat', 'Lychee', 'Madarins', 'Malanga', 'Mandarin Oranges', 'Mangos', 'Mulberries', 'Mushrooms', 'Napa', 'Nectarines', 'Okra', 'Onion', 'Oranges', 'Papayas', 'Parsnip', 'Passion Fruit', 'Peaches', 'Pears', 'Peas', 'Peppers', 'Persimmons', 'Pineapple', 'Plantains', 'Plums', 'Pomegranate', 'Potatoes', 'Prickly Pear', 'Prunes', 'Pummelo', 'Pumpkin', 'Quince', 'Radicchio', 'Radishes', 'Raisins', 'Raspberries', 'Red Cabbage', 'Rhubarb', 'Romaine Lettuce', 'Rutabaga', 'Shallots', 'Snow Peas', 'Spinach', 'Sprouts', 'Squash', 'Strawberries', 'String Beans', 'Sweet Potato', '', 'Tangelo', 'Tangerines', 'Tomatillo', 'Tomato', 'Turnip', 'Ugli Fruit', 'Water Chestnuts', 'Watercress', 'Watermelon', 'Waxed Beans', 'Yams', 'Yellow Squash', 'Yuca/Cassava', 'Zucchini Squash', 'Ajowan', 'Allspice', 'Amchur', 'Angelica', 'Anise', 'Annatto', 'Asafoetida', 'Barberry', 'Basil', 'Bay Leaf', 'Bee balm (Bergamot, Monarda)', 'Black Cumin', 'Black Lime (Loomi)', 'Boldo (Boldina)', 'Borage', 'Bush Tomato (Akudjura)', 'Calamus (Sweet Flag)', 'Candlenut', 'Capers', 'Caraway', 'Cardamom', 'Cassia', 'Cayenne Pepper', 'Celery', 'Chervil', 'Chicory', 'Chile Varieties', 'Chili', 'Chives', 'Cilantro', 'Cinnamon', 'Clove', 'Coriander', 'Cubeb', 'Cumin', 'Curry Leaf (Kari)', 'Dill', 'Elder (Elder Flower & Elderberry)', 'Epazote', 'Fennel', 'Fenugreek', 'Galangal', 'Garlic', 'Ginger', 'Hoja Santa', 'Horseradish', 'Hyssop', 'Jamaican Sorrel', 'Juniper', 'Kaffir Lime', 'Kokum', 'Lavender', 'Lemon Balm', 'Lemon Grass', 'Lemon Myrtle', 'Lemon Verbena', 'Licorice', 'Loomi (Black Lime)', 'Lovage', 'Mace', 'Mahlab', 'Marjoram', 'Mastic', 'Melegueta Pepper (Grains of Paradise)', 'Mint', 'Mountain Pepper (Tasmanian Pepper)', 'Mustard', 'Myrtle', 'Nigella', 'Nutmeg', 'Onion', 'Orris Root', 'Paprika', 'Parsley', 'Pepper', 'Poppy Seed', 'Rosemary', 'Saffron', 'Sage', 'Sassafras', 'Savory', 'Scented Geranium', 'Screw-pine (Pandan)', 'Sesame', 'Soapwort', 'Sorrel', 'Star Anise', 'Sumac', 'Szechwan Pepper', 'Tamarind', 'Tarragon', 'Thyme', 'Turmeric', 'Vanilla', 'Wasabi', 'Watercress', 'Wattleseed', 'Zedoary', 'Olive oil', 'Vegetable oil', 'Sesame oil', 'Balsamic vinegar', 'Cider vinegar', 'Red wine vinegar', 'Rice vinegar', 'Salt', 'Pepper', 'Ginger', 'Cumin ', 'Smoked paprika', 'Red pepper flakes', 'Chili powder', 'Cayenne pepper', 'Nutmeg', 'Fennel', 'Garlic powder', 'Thyme', 'Sage', 'Dill', 'Oregano', 'Honey', 'Maple syrup', 'Potatoes', 'Onion',																								
    ];
    function split( val ) {
      return val.split( /,\s*/ );
    }
    function extractLast( term ) {
      return split( term ).pop();
    }

    $( "#tags" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            availableTags, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
  } );
