function showMyImage(id) {
	var image = document.getElementById(id);
	var modal = document.getElementById("image-popup");
	var image_in_popup = document.getElementById("image-in-popup");
	modal.style.display = "block";
	image_in_popup.src = image.src;
	console.log("got ele");
}
function hide_popup() {
	var modal = document.getElementById("image-popup");
	modal.style.display = "none";
}
