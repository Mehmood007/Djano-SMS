/*
Below code is portable and can be used in any page but just remember few constraints
It supports up to four different class further classes can be added in BG_COLORS Array

Construct PieChart with following arguements
  element_id: Element_id which you want to replace it with PieChart -> String
  labels: What should be label for each chunk -> [String]
  scores: What should be score of each group -> [Number]

Below is sample object creation
new PieChart("fee_piechart", ["Paid", "Unpaid"], [7500, 3000]);

*/
class PieChart {
  static BG_COLORS = ["#36A2EB", "#FF6384", "#FFCE56", "#4CAF50"];

  constructor(element_id, labels, scores) {
    this.element_id = element_id;
    this.labels = labels;
    this.scores = scores;
    this.draw();
  }

  draw() {
    var pieData = {
      labels: this.labels,
      datasets: [
        {
          data: this.scores,
          backgroundColor: PieChart.BG_COLORS,
          borderWidth: 0, // Set borderWidth to 0 to remove borders
        },
      ],
    };

    // Get the canvas element
    var ctx = document.getElementById(this.element_id).getContext("2d");

    new Chart(ctx, {
      type: "pie",
      data: pieData,
      options: {
        legend: {
          display: true,
          position: "top", // You can change the position of the legend (top, bottom, left, right)
        },
      },
    });
  }
}
