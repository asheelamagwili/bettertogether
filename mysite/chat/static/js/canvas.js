
window.addEventListener("load", () => {
    // Gets the canvas
    const canvas = document.querySelector("#canvas");
    // Defines what context were working in
    const ctx = canvas.getContext("2d");
    // Gets the color of the marker
    const red_marker = document.querySelector("#red_marker");
    const blue_marker = document.querySelector("#blue_marker");
    const black_marker = document.querySelector("#black_marker");
    // Event listener that listens when the button is pushed
    red_marker.addEventListener("mousedown", red);
    blue_marker.addEventListener("mousedown", blue);
    black_marker.addEventListener("mousedown", black);
    // Keeps track of the current color
    const current_color = '';

    // Holds start & end positions
    var start = {};
    var end = {};
    var plots = [];

    // Initialize the PubNub API
    var channel = 'my-draw-demo';
    var pubnub = PUBNUB.init({
      publish_key: "pub-c-e77bd0c0-5551-48fd-900b-0528b548d2a3",
      subscribe_key: "sub-c-f3c4a864-170f-11ea-a1d5-ea5a03b00545",
      ssl: true
    });

    // Programmatically resizes to the window
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
  
    // Flag that indicates when you are drawing or not
    let drawing = false;
  
    // Start drawing
    function startDrawing(e){
      drawing = true;
      ctx.beginPath();
      //storeCoordinate(e.clientX,e.clientY, plots);
      draw(e);
    }
  
    // Stop drawing
    function endDrawing(){
      drawing = false;
      ctx.beginPath();
  
      // Send data
      pubnub.publish({
        channel: "pubnub_onboarding_channel",
        message: {
          "plots": plots
        },
        callback: function(m) {
          console.log(m)
        }
      });

      // Empty the array again
      plots = [];

      // Retrieve Data
      pubnub.subscribe({
        channel: ['pubnub_onboarding_channel'],
        message: function(m) {
          console.log(m)
        },
        callback: drawFromStream,

        // Add presence
        presence: function(m){
          var element = document.getElementById('occupancy');
          if(element){
            element.textContent = m.occupancy;
          }
        }
      });

      // Draw the data received from the stream
      //drawFromStream(message);
    }

    // Function to draw the received data
    function drawFromStream(message) {
      if(!message) return;        
  
      ctx.beginPath();
      drawOnCanvas(message.plots);
    }
  
    // Draw on own user the canvas
    function draw(e){
      if(!drawing) return;
  
      // Style the default tool - black & circular
      ctx.lineWidth = 10;
      ctx.lineCap = "round";
      updateColor(current_color);
  
      // Start moving the position
      ctx.lineTo(e.clientX,e.clientY);
      
      // Record starting coordinates
      start.x = e.clientX;
      start.y = e.clientY;
      storeCoordinate(start.x, start.y, plots);

      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(e.clientX,e.clientY);
      storeCoordinate(e.clientX,e.clientY, plots);

      // Record end coordinates
      end.x = e.clientX;
      end.y = e.clientY;
      storeCoordinate(end.x, end.y, plots);
    }
  
    // Listen for a mouse click & release
    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", endDrawing);
    canvas.addEventListener("mousemove", draw);

    // Function to store coordinates into a given array
    function storeCoordinate(xVal, yVal, array) {
      array.push({x: xVal, y: yVal});
    }

    // Function to draw on the canvas in a given array
    function drawOnCanvas(plots) {
      ctx.beginPath();
      ctx.moveTo(plots[0].x, plots[0].y);
    
      for(var i=1; i<plots.length; i++) {
        ctx.lineTo(plots[i].x, plots[i].y);
      }
      ctx.stroke();
    }

    // Functions to change the color of the marker
    function red(e) {
      ctx.strokeStyle = 'red';
      current_color = 'red';
    }

    function blue(e) {
      ctx.strokeStyle = 'blue';
      current_color = 'blue';
    }

    function black(e) {
      ctx.strokeStyle = 'black';
      current_color = 'black';
    }

    function updateColor(color){
      if(color == 'red') {
        document.querySelector("#red_marker").click();
      }

      if(color == 'blue') {
        document.querySelector("#blue_marker").click();
      }

      if(color == 'black') {
        document.querySelector("#black_marker").click();
      }
    }
});