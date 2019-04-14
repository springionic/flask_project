function turn()
{
	var cls =document.getElementById("wrapp").className;
	if(/photo_front/.test(cls))
	{cls=cls.replace(/photo_front/,'photo_back');}
	else
	{cls=cls.replace(/photo_back/,'photo_front');}
	return wrapp.className=cls;
}// JavaScript Document