/*
Below code is portable and can be used in any page but just remember few constraints
It supports up to four different class further classes can be added in BG_COLORS Array

Construct PieChart with following arguements
  element_id: Element_id which you want to replace it with PieChart -> String
  groups: What should be the groups on which items will be divided -> [String]
  categories: Categories lies in each group -> [Number]


Below is sample object to be created
new BarChart("result_barchart",["First Term", "Second Term", "Third Term"], ["English", "Urdu", "Maths"], [[76,89,78],[86,78,81],[65,78,89]]);

*/
class BarChart {
  static BG_COLORS = ["#36A2EB", "#FF6384", "#FFCE56", "#4CAF50"];

  constructor(element_id, categories, labels, dataset) {
    this.element_id = element_id;
    this.labels = labels;
    this.dataset = dataset;
    this.categories = categories;
    this.set_data();
    this.draw();
  }

  set_data() {
    let category_data = [];
    for (let i = 0; i < this.dataset.length; i++) {
      category_data.push({
        label: this.categories[i],
        backgroundColor: BarChart.BG_COLORS[i],
        data: this.dataset[i],
      });
    }
    this.barData = {
      labels: this.labels,
      datasets: category_data,
    };
  }

  draw() {
    console.log(this);
    var ctx = document.getElementById(this.element_id).getContext("2d");

    // Create the grouped bar chart
    new Chart(ctx, {
      type: "bar",
      data: this.barData,
      options: {
        scales: {
          yAxes: [
            {
              ticks: {
                beginAtZero: true,
              },
            },
          ],
        },
        plugins: {
          legend: {
            display: true,
            position: "top",
          },
          group: {
            group: "myGroup",
            xAxisID: "x",
            yAxisID: "y",
          },
        },
      },
    });
  }
}
