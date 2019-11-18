$(function(){
    // 轮播图自动播放
    plant_play();
    move();
})


function plant_play(){
    for(let i = 0; i<$(".plant li").length; i++){
        //获取父元素的宽度，即屏幕宽度，实现不同平台都能自适应屏幕大小小
        let width = $(".plant").innerWidth();
        let str = "url(D:/Read&Listen/front-end/images/book" + i + ".jpg)"
        $(".plant li").eq(i).css("background-image", str);
        $(".plant li").eq(i).css("left", String(i*width)+"px")
    }
    var playTime = setInterval("showAuto()", 5000);
}


function showAuto(){
    let width = $(".plant").innerWidth();
    for(let i=0; i<3; i++){
        let left = $('.plant li').eq(i).offset().left;
        if((left-width)<-width){
            $('.plant li').eq(i).css({
                'left': String(width*1)+'px',
                "zIndex" : "-2",
                'transition': 'left 0s',
        }); 
        }else{
            $('.plant li').eq(i).css('left', );
            $('.plant li').eq(i).css({
                'left': String(Math.round(left-width))+'px',
                'transition': 'left 1s',
            })
        }
    }
}

function move(){
    $(".type").mousedown(function(e){
        console.log('down');
        $(this).mousemove(function(e){
            let pageX = e.pageX;
            let pageY = e.pageY;
            console.log(pageX, pageY);
            $(this).mouseup(function(e){
                
            })
        })
    })
}