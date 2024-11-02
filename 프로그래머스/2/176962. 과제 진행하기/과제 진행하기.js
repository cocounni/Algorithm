function solution(plans) {
  const toMinutes = (time) => {
    const [hours, minutes] = time.split(":").map(Number);
    return hours * 60 + minutes;
  };

  plans = plans.map(([name, start, duration]) => [name, toMinutes(start), Number(duration)]);
  plans.sort((a, b) => a[1] - b[1]);

  const result = [];
  const stack = [];

  for (let i = 0; i < plans.length; i++) {
    const [name, start, duration] = plans[i];
    let endTime = start + duration;

    if (i < plans.length - 1 && endTime > plans[i + 1][1]) {
      const remainingTime = endTime - plans[i + 1][1];
      stack.push([name, remainingTime]);
    } else {
      result.push(name);
      let availableTime = i < plans.length - 1 ? plans[i + 1][1] - endTime : Infinity;

      while (stack.length && availableTime > 0) {
        const [pausedName, pausedTime] = stack.pop();
        if (pausedTime <= availableTime) {
          result.push(pausedName);
          availableTime -= pausedTime;
        } else {
          stack.push([pausedName, pausedTime - availableTime]);
          availableTime = 0;
        }
      }
    }
  }

  return result;
}
