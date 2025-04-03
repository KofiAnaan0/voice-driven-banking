$(document).ready(function () {
	// Show text based on selected language when record button is clicked
	$("#record").click(function () {
		if ($("#username").val() == "") {
			$("#username").css("border-color", "red");
		} else {
			// Get the selected language
			var selectedLanguage = $("#language").val();

			// Hide all language texts and headers first
			$(".language-text").hide();
			$(".modal-header").hide();

			// Update the Start button text based on language
			if (selectedLanguage == "english") {
				$("#english-text").show();
				$("#english-header").show();
				$("#start").text("Start");
			} else if (selectedLanguage == "hindi") {
				$("#hindi-text").show();
				$("#hindi-header").show();
				$("#start").text("प्रारंभ करें");
			} else if (selectedLanguage == "swahili") {
				$("#swahili-text").show();
				$("#swahili-header").show();
				$("#start").text("Anza");
			} else if (selectedLanguage == "zulu") {
				$("#zulu-text").show();
				$("#zulu-header").show();
				$("#start").text("Qala");
			} else {
				// If no language selected, show English as default
				$("#english-text").show();
				$("#english-header").show();
				$("#start").text("Start");
			}

			// Show the modal
			$("#myModal").modal("show");
		}
	});

	$("#start").click(function () {
		// Get the selected language to determine the "listening" text
		var selectedLanguage = $("#language").val();

		// Update the button text to show "listening" in the appropriate language
		if (selectedLanguage == "english") {
			$(this).html("Listening...");
		} else if (selectedLanguage == "hindi") {
			$(this).html("सुन रहा है...");
		} else if (selectedLanguage == "swahili") {
			$(this).html("Inasikiliza...");
		} else if (selectedLanguage == "zulu") {
			$(this).html("Iyalalela...");
		} else {
			$(this).html("Listening...");
		}

		let name = document.getElementById("username").value;
		let language = document.getElementById("language").value;

		// Pass both name and language to the server
		$.get("/test", { name: name, language: language }).done(function () {
			// Show "done" in the appropriate language
			if (selectedLanguage == "english") {
				$("#start").html("Done");
			} else if (selectedLanguage == "hindi") {
				$("#start").html("पूर्ण");
			} else if (selectedLanguage == "swahili") {
				$("#start").html("Imekamilika");
			} else if (selectedLanguage == "zulu") {
				$("#start").html("Kwenziwe");
			} else {
				$("#start").html("Done");
			}

			setTimeout(function () {
				$("#myModal").modal("hide");
			}, 1000);
		});
	});
});
