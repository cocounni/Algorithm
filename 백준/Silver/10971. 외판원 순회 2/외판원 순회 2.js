const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
let city = [];
let min = 987654321;
let check = new Array(10).fill(false);
rl.on('line', function (line) {
  input.push(line);
})
  .on('close', async function () {
  // 답안 작성
  let answer =0;  
  let n = input.splice(0,1);
  //입력 받은 도시문자열 배열화
  input.reduce((acc,cur)=>{
    city.push(cur.split(' '));
  },'')
  
  tsp(n);  
  console.log(min);
  process.exit();
});

//시작 노드값을 따로 지정하지 않기 위한 시작용 반복문
let tsp = function(n){
  for(let i=0;i<n;i++){
    re(0,n,i,i,0);  
  }  
}

//무한정 경로값을 합하는 재귀
let re = function(cnt,n,start,next, sum){
  //재귀 중 시작으로 돌아옴을 판별하는 브레이크 조건
  if(cnt==n&&start==next){    
    min = Math.min(min,sum);
    return;
  }
  //모든 경우의 수열 반복문
  for(let i=0;i<n;i++){
    //방문 한 적이 없고 해당 경로 값이 0이상일때
    if(!check[i]&&city[next][i]*1>0){   
      check[i] = true;
      if(sum + city[next][i]*1 < min){
        re(cnt+1,n,start,i,sum+city[next][i]*1)
      }
      check[i] = false;
    }
  }
}