var data = `{ 
    "gross_scores": {
        "1": {
		"name": "Jack Sullivan",
		"scores": ["3", "4", "5", "6", "6", "4", "8", "10", "2", "13", "4", "3", "4", "5", "3", "2", "1", "1"],
		"front_total": "48",
		"back_total": "36",
		"total": "84",
		"handicap": "19"
	},
	"2": {
		"name": "Jim Bob Cooter",
		"scores": ["3", "4", "5", "6", "6", "4", "8", "10", "2", "13", "4", "3", "4", "5", "3", "2", "3", "5"],
		"front_total": "48",
		"back_total": "36",
		"total": "90",
		"handicap": "19"
	}
    }
}`;

// Element IDs in year_scores.html
var editScoresButtonId = "sparta-edit-scores-btn";
var submitScoresButtonId = "sparta-submit-scores-btn";
var addRowButtonId = "sparta-add-row-scores-btn";
var grossScoresTableId = "sparta-gross-scores-table";
var netScoresTableId = "sparta-net-scores-table";
// Speical var to keep track of rows
var editableRowId = "sparta-editabled-table-row-id-";

// Listen for clicks on our buttons

const Listen = (doc) => {
    return {
        on: (type, selector, callback) => {
            doc.addEventListener(type, (event)=>{
                if(!event.target.matches(selector)) return;
                callback.call(event.target, event);
            }, false);
        }
    }
};

Listen(document).on('click', '.sparta-btn', function (e) {
   console.log(e.target.id + " clicked mf");
   if (e.target.id === editScoresButtonId) {
      console.log("edit scores button pressed");
      editGrossScoresButtonClicked(e.target.id);

   } else if (e.target.id == submitScoresButtonId) {
      console.log("Submit scores button pressed");

   } else if (e.target.id == addRowButtonId) {
      console.log("Add Row Button ID Clicked");
      addEmptyEditableRow(grossScoresTableId);

   } else if (e.target.id == addRowButtonId) {
      console.log("Remove Row Button ID Clicked");
      addEmptyEditableRow(grossScoresTableId);
   
   } else if (e.target.id.startsWith(editableRowId)) {
      var rowId = e.target.id;
      console.log("editable row button clicked! " + rowId); 
      removeRowById(grossScoresTableId, rowId)
   }


});

// Enable edit mode
function editGrossScoresButtonClicked(btnId) {
   fillScoreSheetTable(gross_scores, grossScoresTableId, true); 
   var submitButton = document.getElementById(submitScoresButtonId);
   var addButton = document.getElementById(addRowButtonId);
   var editButton = document.getElementById(editScoresButtonId);
   
   submitButton.disabled = false;
   submitButton.hidden = false;
   addButton.disabled = false;
   addButton.hidden = false; 
   editButton.disabled = true;
}

function addCell(tr, text) {
   addCell(tr, text, false);
}

function addCell(tr, text, editable) {
   var td = tr.insertCell();
   td.textContent = text;
   if (editable) {
      td.contentEditable = "true";
   }
   return td;
}

function removeRowById(tableId, rowId) {
   var row = document.getElementById(rowId);
   console.log(row);
   row.parentNode.removeChild(row);
}

// TODO cleanup and genericise add row logic.

function addEmptyEditableRow(tableId) {
   var tableBody = document.getElementById(tableId);
   var row = tableBody.insertRow();
 
   // Very hacky way to get the highest index currently in the table.
   var rowId = -1
   var cells = tableBody.getElementsByTagName('tr');
   for (let cell of cells) {
      console.log(cell);
      if (cell.id.startsWith(editableRowId)) {
         var id = parseInt(cell.id.split(editableRowId)[1]);
         if (id > rowId) {
            rowId = id;
         } 
      }
   }
   // Add one to the highest
   rowId += 1;

   // Name 
   addCell(row, "Fake Name1", true);
   // Add Front 9 Scores
   for ( let i = 0; i < 9; i++) {
      addCell(row, "0", true);
   }
   // Front 9 Total
   addCell(row, "--", false);
   for ( let i = 9; i < 18; i++) {
      addCell(row, "0", true);
   }
   // Add Back 9 Score/Total Score
   addCell(row, "--", false);
   addCell(row, "--", false);
        
   td = addCell(row, "", false);
   td.innerHTML = '<button id="' + editableRowId + rowId + '" class="sparta-btn btn btn-info btn-fill btn-wd">Delete</button>'
   td.class = "sparta-delete-row-btn";
   row.id = editableRowId + rowId;
}

// Function for filling score tables
function fillScoreSheetTable(scores, tableId, editable) {
   var tableBody = document.getElementById(tableId);

   // Clear out table
   tableBody.innerHTML="";

   var index = 0;
   for (player in scores) {
      var row = tableBody.insertRow();
      addCell(row, scores[player]["name"], editable);

      var front9Score = 0;
      var back9Score = 0;
      // Add Front 9 Scores
      for ( let i = 0; i < 9; i++) {
         score = scores[player]["scores"][i];
         addCell(row, score, editable);
         front9Score += parseInt(score);
      }
      // Add Front 9 Total Score
      addCell(row, front9Score);
      // Add Back 9 Scores
      for ( let i = 9; i < 18; i++) {
         score = scores[player]["scores"][i];
         addCell(row, score, editable);
         back9Score += parseInt(score);
      }
      // Add Back 9 Total Score
      addCell(row, back9Score);
      addCell(row, front9Score + back9Score);

      if(editable) {
         td = addCell(row, "", false);
         td.innerHTML = '<button id="' + editableRowId + index + '" class="sparta-btn btn btn-info btn-fill btn-wd">Delete</button>'
         td.class = "sparta-delete-row-btn";
      } 

      // Add an index so we can keep track of which delete row this is.
      row.id = editableRowId + index;


      index++;
      console.log("Player " + scores[player]["name"] + " scored " + front9Score+back9Score);
   }
}

//var scoresJson = JSON.parse(data);
//var gross_scores = scoresJson.gross_scores;

/*
fillScoreSheetTable(gross_scores, grossScoresTableId, false); 
fillScoreSheetTable(gross_scores, netScoresTableId, false);
*/



 
