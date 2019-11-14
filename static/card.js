function cardcreate(imglink,id){
var pardiv=document.getElementById('mydiv');
var div=document.createElement('div');
div.setAttribute('class','zoom main-card');
div.setAttribute('style',"width:200px; float: left; ;border: 2px; border-radius:15px; margin-left:10px;margin-bottom:10px");
div.setAttribute('id',id);
div.setAttribute('onclick','onlick(this.id)')
var img=document.createElement('img')
img.setAttribute('class','main-picture');
img.setAttribute('id','main-pic');
img.setAttribute('src',imglink);
img.setAttribute('style',"border: 2px; border-radius:15px");
div.append(img);
pardiv.append(div);
};