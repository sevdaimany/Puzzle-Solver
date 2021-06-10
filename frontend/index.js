async function main () {
  let resultJson = await eel.main () ();
  let result = JSON.parse (resultJson);
  let steps = result["steps"];
  let puzzle = result["puzzle"];
  console.log(steps);
  console.log(puzzle);

}

main ();
