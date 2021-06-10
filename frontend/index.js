const {Engine, Render, Runner, World, Bodies, Body, Events} = Matter;
const engine = Engine.create ();
const {world} = engine;
let render;
let runner;
let robot;
let butters = [];
// const unitLengthX = 110;
// const unitLengthY = 110;
// const unitLengthX  = 0;
// const unitLengthY  = 0;


function table (graph, horizontal, vertical) {
  const cellsHorizontal = horizontal;
  const cellsVertical = vertical;
  // const width = cellsHorizontal * 110;
  // const height = cellsVertical * 110;
  const width = 1100;
  const height = 700;
  const unitLengthX = width / horizontal;
  const unitLengthY = height /vertical ;



  engine.world.gravity.y = 0;
  render = Render.create ({
    element: document.body,
    engine: engine,
    options: {
      wireframes: false,
      width,
      height,
      wireframes: false,
      background: '#f8f5f1',
      // background : '#bbdfc8',
    },
  });
  Render.run (render);
  runner = Runner.create ();
  Runner.run (runner, engine);

  const walls = [
    Bodies.rectangle (width / 2, 0, width, 2, {isStatic: true}),
    Bodies.rectangle (0, height / 2, 2, height, {isStatic: true}),
    Bodies.rectangle (width, height / 2, 2, height, {isStatic: true}),
    Bodies.rectangle (width / 2, height, width, 2, {isStatic: true}),
  ];
  World.add (world, walls);

  // for (const [key, value] of Object.entries (graph)) {
  for (const [x, y, value] of graph) {
    console.log (x, y, value);
    let indexRow = x;
    let indexColumn = y;
    let type = value;
    if (type === 1) {
      const dest = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX - 10,
        unitLengthY - 10,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: './icons/1.png',
              xScale: 0.06,
              yScale: 0.06,
            },
          },
        }
      );
      World.add (world, dest);
    } else if (type === 0) {
      const dest = Bodies.rectangle (
        (indexColumn + 0.5) * unitLengthX,
        (indexRow + 0.5) * unitLengthY,
        unitLengthX - 10,
        unitLengthY - 10,
        {
          isStatic: true,
          render: {
            sprite: {
              texture: './icons/0.png',
              xScale: 0.06,
              yScale: 0.06,
            },
          },
        }
      );
      World.add (world, dest);
    }
  }
}

async function main () {
  let resultJson = await eel.main () ();
  let result = JSON.parse (resultJson);
  let steps = result['steps'];
  let puzzle = result['puzzle'];
  let len = result['len'];
  console.log (steps);
  console.log (puzzle);
  table (puzzle, len, len);
}

main ();
