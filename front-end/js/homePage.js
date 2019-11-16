$(function(){
    // 轮播图自动播放
    plant_play();
    // showAuto()
})
// cont[0]放的是轮播图循环数
var cont = [1];

function plant_play(){
    for(let i = 0; i<$(".plant li").length; i++){
        let str = "url(D:/Read&Listen/front-end/images/book" + i + ".jpg)"
        $(".plant li").eq(i).css("background-image", str)
    }
    let cont = 1

    var playTime = setInterval("showAuto()", 1000);

}



function showAuto(){
    if(cont[0]==5){
        cont[0]=0;
    }
    for(let i=0; i<$(".plant li").length; i++){
        // console.log(i);
        let left = $(".plant").eq(i).offset();
        console.log(left);
    }
    let width = $(".plant").eq(i).innerWidth();
    $(".plant ul").css({
        "left": String(-width*cont[0])+"px",
        "transition": "left 0.5s"
    });
    
    cont[0]+=1;
}