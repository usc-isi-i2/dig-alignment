<!DOCTYPE html><html
    xmlns="http://www.w3.org/1999/xhtml"
    xmlns:fb="https://www.facebook.com/2008/fbml"
    xmlns:addthis="https://www.addthis.com/help/api-spec"
    >
<head>
    <meta charset="utf-8">
    <title>ALCON PHARMACEUTICALS LTD. et al v. DR. REDDYS LABORATORIES, INC. et al | Patexia.com</title>    <meta http-equiv="Content-type" content="text/html;charset=UTF-8" >
<meta name="keywords" content="Patent Search, Patent, Intellectual property, Patent Community, Prior art search, Intellectual Property Community" >
<meta name="description" content="Details of the lawsuit ALCON PHARMACEUTICALS LTD. et al v. DR. REDDYS LABORATORIES, INC. et al" >    <!--<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>-->
    

    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.7/jquery-ui.min.js"></script>
<script type="text/javascript" src="/js/compiled/applicationd3157f2f0212a80a5d042c127522a2d5.js"></script>
<script type="text/javascript">
    //<!--
$(document).ready(function() {
    Application.init();Application.initRoles(["guest"]);
        $('#attorneyUp').click(function(){
        var href = $(this).attr('href');
        var attorneyBlock = $('#attorneyBlock');
//        attorneyBlock.animate({opacity: 1, height: 'hide'}, 1000);
        var ajaxLoader = {
            send :
                function() {
                    if(typeof this.request !== 'undefined') {
                        this.request.abort();
                    }
                    this.request =
                    $.ajax({
                        url: href,
                        beforeSend : function() {
                            if ($("#unclickableDiv").length < 1) {
                                var coveredDiv = '<div id="unclickableDiv" style="text-align: center;"><div style="margin-top: 200px;"><div class="loaderBox" style="margin: auto;"><h1 style="width: 100%">Loading</h1><img src="/images/general/preloader.gif"/></div></div></div>';
                                $('body').append(coveredDiv);
                            }
                            $('#unclickableDiv').show();
                            $('#unclickableDiv').click(function(){ajaxLoader.request.abort(); return true;});
                        },
                        success: function(response) {
                            if (response.status == Application.AJAX_OK) {
                                Application.flashMessager(response.message);
                                attorneyBlock.html(response.html);
                            } else {
                                if(response.message) {
                                    Application.flashMessager(response.message);
                                }
                                else {
                                    Application.flashMessager('Error Occurred');
                                }
                            }
                        },
                        complete : function() {
                            $('#unclickableDiv').hide();
                            attorneyBlock.animate({opacity: 1, height: 'show'}, 2000);
                        },
                        dataType : 'json'
                    });
                }
        }
        ajaxLoader.send();
        return false;
    });

    $('.showLawsuitsByCompany').lawsuitCompanies();
    $('.showLawsuitsByAttorneys').lawsuitAttorneys();

    $('.statusChange').change(function(){
        var litId = '59342';
        var status = $(this).val();

        request=$.post
        (
            "/changelawsuitstatus",
            {
                'litId':litId,
                'status':status
            },
            function(response)
                {
                if (response.status == Application.AJAX_OK)
                {
                    if(response.msg)
                    {
                    Application.flashMessager(response.msg);
                    }
                }
                else
                {
                    if(response.msg)
                    {
                        Application.flashMessager(response.msg);
                    }
                }

            },
            "json"
        );
    });

        $('.commentsHolder').comments(59342,"",
	{	
		type: 2,
		perPage: 10,
		onUpdate: function(){ $('.likeLink').like({canLike: false}); }
	});

	$('.overtext').overtext();
	
	$('#saveBtn').click(function(){
    	$('#FormComment').submit();
    });
    
	$(".upa-arrow").live('click',function(){
    	var list = $(this).parent().children('.userActionsList');
        list.toggle();
    });

    $('.patentsSum').summaryShowSubCont({
    parentHold: '.patentsSummaryBox',
    animateHold: '.patentsSummarySubTxt '
});

	$('.npeChange').click(function(e){
	
    	var lwId=$(this).attr('id');
    	var clusterId=$(this).val();
        var type = $(this).attr('rel');
    	var status;
    	if ($(this).is(':checked')){
    		status=1;
    	}else{
    		status=0;
    	}
        request=$.post
        (
            '/lawsuits/npestatus/1',
            {lw:lwId,claster:clusterId,status:status,type:type},
            function(response)
            {
                if (response.status == Application.AJAX_OK)
                {
                    if(response.message)
                    {
                        Application.flashMessager(response.message);
                    }
                }
                else
                {
                    if(response.message)
                    {
                        Application.flashMessager(response.message);
                    }
                }
            },
            "json"
        );
    });

    $('.individualChange').click(function(e){

        var lwId=$(this).attr('id');
        var clusterId=$(this).val();
        var type = $(this).attr('rel');
        var status;
        if ($(this).is(':checked')){
        status=1;
        }else{
        status=0;
        }
        request=$.post
        (
        '/lawsuits/individualstatus/1',
        {lw:lwId,claster:clusterId,status:status,type:type},
        function(response)
        {
        if (response.status == Application.AJAX_OK)
        {
        if(response.message)
        {
        Application.flashMessager(response.message);
        }
        }
        else
        {
        if(response.message)
        {
        Application.flashMessager(response.message);
        }
        }
        },
        "json"
        );
    });
	
	

        $('#selectsearch').change(function(){
        var selectParam = $(this).val();
        if (selectParam == 'ArticlesVideos') {
            selectParam = 'Articles/Videos';
        }

        $('#keywordSearch').val('Search '+selectParam);
        $('#keywordSearch').searchOverText();
        selectParam = selectParam.toLowerCase();
    });

    $('#keywordSearch').searchOverText();

    $('#frontSearch-form').submit(function()
    {
        var value = $('#keywordSearch').val();
        var selectParam = $('#selectsearch option:selected').val();
        selectParam = selectParam.replace("/", "");
        var url = $('option.'+selectParam+'SearchOption').attr('rel');

        if (!value) {
            return false;
        }

        url = url.replace("$s", value);
        window.location.href = url;
        return false;
    });

        $('.login').click(function(){
    	if($(this).hasClass('open')){
    		$(this).removeClass('open');
    		$('#logInHolder').hide();
    	}else{
    		$(this).addClass('open');
    		$('#logInHolder').show();
    	}
    });

    $('.loginInfo').click(function(){
    	var parent = $(this).parent();
    	parent.children('.setingsBox').toggle();
    	parent.toggleClass("open");
    });

    
});
    //-->
</script>    <link href="/css/compiled/applicationd3157f2f0212a80a5d042c127522a2d5.css" media="screen" rel="stylesheet" type="text/css" >
<link href="/images/general/favicon.ico" rel="shortcut icon" >
<!--[if IE]> <link href="/css/ie.css" media="screen" rel="stylesheet" type="text/css" ><![endif]-->        <script type="text/javascript">
	var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-16949080-1']);
    _gaq.push(['_trackPageview']);

    (function() {
      var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
      ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
      var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>    <!--[if gte IE 8]>
    <style>
        .contestAnswerForm .userBlogTable td{float:left; }
        .contestAnswerForm .userBlogTable .cke_editor td{float:none;}
    </style>
    <![endif]-->

</head>
<body class="defaultModule lawsuitsController viewAction     ">
<div id="fb-root"></div>
<script>
    window.fbAsyncInit = function() {
        FB.init({"appId":"158230814236392","key":"1bbc7285f19f9c2ed815d843c1e908d6","secret":"aee7aa0799afe2961f964901a3acc7e7","cookie":true,"logging":false,"channelUrl":"\/\/patexia.com\/facebook_channel.php","status":false,"xfbml":false,"oauth":true});
    };

    // Load the SDK Asynchronously
    (function(d){
        var js, id = 'facebook-jssdk'; if (d.getElementById(id)) {return;}
        js = d.createElement('script'); js.id = id; js.async = true;
        js.src = "//connect.facebook.net/en_US/all.js";
        d.getElementsByTagName('head')[0].appendChild(js);
    }(document));
</script><div id="pageLayout" class="clearfix">
            <div id="topWrapper">
            <div id="topHolder">
                <div id="top" class="pageLayout clearfix">
                    <div id="Logo">
                        <a href="https://www.patexia.com"></a>
                    </div>
                    <div id="contentTop" class="clearfix">
                        <nav>
                            <div id="mainMenu">
                                <ul class="navigation">
    <li>
        <a id="menu-ipContest" class="highlighted showDialog" href="/contestslist">Contest</a>
        <ul>
            <li>
                <a class="highlighted showDialog" href="/contestslist">Contests</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/contest_guide.html">Contest Guide</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/general_contest_rules.html">Rules</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/leaderboard">Leaderboard</a>
            </li>
        </ul>
    </li>
    <li>
        <a id="menu-ipConnect" title="Your source for information and updates relating to innovation and IP" class="highlighted" href="/connect">Connect</a>
        <ul>
            <li>
                <a class="highlighted showDialog" href="/connect">Connects</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/connect_guide.html">Connect Guide</a>
            </li>
        </ul>
    </li>
    <li>
        <a id="menu-ipCommunity" title="Your source for information and updates relating to innovation and IP" class="highlighted" href="/newsfeed">Community</a>
        <ul>
            <li>
                <a id="menu-topCom" href="/newsfeed">Newsfeed</a>
            </li>
            <li>
                <a id="menu-topInterest" href="/groups/list">Interests</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/leaderboard">Leaderboard</a>
            </li>
            <li>
                <a class="highlighted showDialog" href="/community_guide.html">Community Guide</a>
            </li>
        </ul>
    </li>
    <li>
        <a href="/ip-research">Research</a>
        <ul>
            <li>
                <a href="/ip-research">Patents</a>
            </li>
            <li>
                <a href="/ip-research/lawsuits">Lawsuits &amp; PTAB</a>
            </li>
            <li>
                <a class="hideInLeftPanel" href="/ip-research/statistic/assignees">Statistics</a>
            </li>
            <li>
                <a class="hideInLeftPanel" href="/research_guide.html">Research Guide</a>
            </li>
        </ul>
    </li>
</ul>                            </div>
                        </nav>
                    </div>
                    <div class="searchbx">
                        <form id="frontSearch-form">
<div class="search">
    	<div class="search_mid">
	<div class="selectBox">
		 <select id="selectsearch" name="selectsearch" class="styledSelect" style="display: none;">
             <option class ="PatentsSearchOption" rel="/ip-research/patents/keyword/$s" value="Patents"  >Patents</option><option class ="LawsuitsSearchOption" rel="/ip-research/lawsuits/keyword/$s" value="Lawsuits" selected="selected" >Lawsuits</option><option class ="ArticlesVideosSearchOption" rel="/newsfeed/keyword/$s" value="Articles/Videos"  >Articles/Videos</option><option class ="PeopleSearchOption" rel="/user/list/keyword/$s" value="People"  >People</option><option class ="CompaniesSearchOption" rel="/companies/list/keyword/$s" value="Companies"  >Companies</option><option class ="GroupsSearchOption" rel="/groups/list/keyword/$s" value="Groups"  >Groups</option><option class ="ContestsSearchOption" rel="/contestslist/keyword/$s" value="Contests"  >Contests</option>		</select>  
	</div>
	<!-- <div class="searchInput"> -->
		<input type="text" id="keywordSearch"  value="Search Lawsuits" name="keyword" maxlength="255"  />
	<!-- </div> -->
	<button class="searchbtn" name="submit" type="submit"></button>			
    </div>
        <div class="search_right"></div>
    </div>				
</form>                    </div>
                                        <div id="userBox">
                        

	    <!-- <div class="guest">
    	<div class="leftColUserBox">
            <div class="welcome clearfix">
                <ul class="guest-nav">
                    <li><a href="/user/register"></a></li>
                    <li><a href="/user/login"></a></li>
                </ul>
            </div> --><!--END welcome-->
        <!--</div> --><!--END leftColUserBox-->
    <!--</div> --><!--END guest-->
    <ul class="rightmenu">
    		             <li class="rightmenuBorder"><a href="/user/invitation">Sign Up</a></li>                             <li class="user-logn" ><a href="/user/login">Member Log In</a></li>
                <!--<li class="li-logn" ><a href="/linkedin" style="margin: 0px; padding: 10px 10px 6px;"><img src="/images/general/linkedin.png" /></a></li>-->
            
    </ul><!-- Guest Section -->
    

<style>
    .business-member{
        margin-bottom: 40px !important;
    }
</style>                    </div>
                </div>

            </div>
        </div>
                <div id="pageTitle" class="businessMemberPageTitle">
                                                Patexia. <span>Research</span>                                     </div>
        <div id="contentWrapper" style="padding-top:60px;"  >
        
<script>
	$(function(){
        $('.headingbar').show();
		// Set starting slide to 1
		var startSlide = 1;
		// Get slide number if it exists
		if (window.location.hash) {
			//startSlide = window.location.hash.replace('#','');
		}
		// Initialize Slides
		$('#slides').slides({
			preload: true,
			preloadImage: '',
			generatePagination: true,
			play: 10000,
			pause: 2500,
			hoverPause: true,
			// Get the starting slide
			start: startSlide,
			animationComplete: function(current){
				// Set the slide number as a hash
				//window.location.hash = '#' + current;
			}
		});
	});
</script>


	<script type="text/javascript" src="//www.hellobar.com/hellobar.js"></script>
<script type="text/javascript">
    new HelloBar(64274,94173);
</script> 

<div class="headingbar">
	




    <!--<div id="containerslider">
        <div id="slides">
            <div class="slides_container">
                <div class="slide">
                    <span class="left">Join Patexia’s community of researchers, businesses, and IP professionals. <a href="/about_us.html">Learn More &raquo;</a> </span>
                </div>
                
                <div class="slide">
                    <span class="left">Earn rewards and gain exposure with Patent Study. <a href="/contests/greenhouse">VIEW LATEST CONTEST &raquo;</a> </span>
                    
                </div>
                
                <div class="slide">
                    <span class="left">Read the latest in innovation & intellectual property news and analysis. <a href="/newsfeed">GO TO NEWSFEED &raquo;</a> </span>
                    
                </div>
                
                <div class="slide">
                    <span class="left">Get unlimited access to IP research and data visualization tools.<a href="/ip-research">GO TO LATEST RESEARCH ENTRY &raquo;</a> </span>
                    
                </div>
            </div>
       	</div>
        <span class="right" style="padding:0 0 0 15px; border-left:1px solid #ccc;"> <a href="/user/invitation/forward/L2xhd3N1aXRzL0FMQ09OLVBIQVJNQUNFVVRJQ0FMUy1MVEQtZXQtYWwtdi1EUi1SRUREWVMtTEFCT1JBVE9SSUVTLUlOQy1ldC1hbC1pZC01OTM0Mg%3D%3D">Request An Invitation</a> or <a href="/user/login/forward/L2xhd3N1aXRzL0FMQ09OLVBIQVJNQUNFVVRJQ0FMUy1MVEQtZXQtYWwtdi1EUi1SRUREWVMtTEFCT1JBVE9SSUVTLUlOQy1ldC1hbC1pZC01OTM0Mg%3D%3D">Log In</a> </span>
	</div>-->
</div>

<!--
<div class="joinUs">
    <h4>Join Patexia's community of researchers, businesses, and IP professionals.</h4>
    <div class="joinBody">
        <p>Read the latest in innovation & intellectual property news; network with professionals; use our research tools and <br />
        win money and gain exposure in Patexia's Contests.</p>
        <a href="">Sign Up</a>
        or <a href="">Log In</a>
    </div>
</div> -->
<div class="clearfix"></div>

        <div id="content" class="pageLayout">
                                                                
            
                        
                            <div id="leftCol"
                                        >
                    <div class="leftWrapper">
                        <div class="leftColItem"><div class="patentBlock">
    <span class="pictureWrapper size200_"><a href="/lawsuits/ALCON-PHARMACEUTICALS-LTD-et-al-v-DR-REDDYS-LABORATORIES-INC-et-al-id-59342"><img class="userPicture" src="/images/general/no_picture/200_lawsuit.png" id="9671d73a"></a></span>
<script>
    var img = document.createElement('img');
    img.src = '/images/general/no_picture/200_lawsuit.png';
//    img.onload = function(){
//        document.getElementById('9671d73a').src = this.src;
//    }
    img.onerror = function(){
        document.getElementById('9671d73a').src = '/images/general/no_picture/200_patent.png';
    }
</script>    	<div class="patentdetailBox">
        <div class="patentDetailsHead ">
            <strong>Case number</strong>
            3:2015-cv-05756        </div>    
    </div>
</div>
</div><div class="leftColItem"><div class="userViewNavigation clearfix">
	
	<ul class="userProfileNav">
		<li>
			<h3>Lawsuits</h3>
			<ul class="userProfileSub">
    <li>
        <a href="/lawsuits/ALCON-PHARMACEUTICALS-LTD-et-al-v-DR-REDDYS-LABORATORIES-INC-et-al-id-59342">Summary</a>
    </li>
    <li>
        <a href="/lawsuits/ALCON-PHARMACEUTICALS-LTD-et-al-v-DR-REDDYS-LABORATORIES-INC-et-al-id-59342/documents">Documents</a>
    </li>
    <li>
        <a href="/lawsuits/ALCON-PHARMACEUTICALS-LTD-et-al-v-DR-REDDYS-LABORATORIES-INC-et-al-id-59342/discussions">Discussions</a>
    </li>
</ul>		</li>
	</ul>
</div></div>                    </div>
                </div>
            
            <div id="middleCol" class="wideRightColumn"                                >
                                <div class="lawsuitDocuments clearfix">
	
	
<h1>ALCON PHARMACEUTICALS LTD. et al v. DR. REDDYS LABORATORIES, INC. et al > Summary</h1>
<div class="patentsSummaryBox clearfix">
   
    <div class="patentsSummaryTxt clearfix">
        <p><strong>Court Case Number</strong> 3:2015-cv-05756</p>
        <p><strong>Filling Date</strong> Jul 24, 2015</p>
                <p><strong>Court</strong> New Jersey District Court</p>
                    <p><strong>Status</strong> Unknown</p>
            </div>
</div>
    
    <div class="patentsSummaryBox clearfix">
        <div class="patentsSummaryTitle clearfix">
            <h3>Plaintiff</h3>
                        	<span class="patentsSum">3</span>
                    </div>
        
        
        
                
                    
                	                    						        <div class="patentsSummaryTxt clearfix">
					            <p><a href="/companies/alcon-research-ltd-us">Alcon Research Ltd (US)</a>					                                              </p>
					        </div>
                    	                                        					            <div class="patentsSummarySubTxt clearfix">
				               	 <p>        	
				                   	<p><a href="/companies/acon-laboratories-inc-us">Acon Laboratories Inc (US)</a> 
				                   					                   	 </p>
				               	</p>
                            </div>
                    	                                        					            <div class="patentsSummarySubTxt clearfix">
				               	 <p>        	
				                   	<p><a href="/companies/alcon-pharmaceuticals-ltd-us">Alcon Pharmaceuticals Ltd (US)</a> 
				                   					                   	 </p>
				               	</p>
                            </div>
                    	                                </div>
            </div>



	<div class="patentsSummaryBox clearfix">
        <div class="patentsSummaryTitle clearfix">
            <h3>Defendant</h3>
                        	<span class="patentsSum">2</span>
                    </div>

        
            
                                                <div class="patentsSummaryTxt clearfix">
                        <p><a href="/companies/dr-reddy-s-laboratories-inc-us">Dr Reddy S Laboratories Inc (US)</a>                                                    </p>
                    </div>
                                                                <div class="patentsSummarySubTxt clearfix">
                        <p>
                        <p><a href="/companies/dr-reddys-laboratories-ltd-us">Dr Reddys Laboratories Ltd (US)</a>                                                    </p>
                        </p>
                    </div>
                                        <!--</div>-->
                    </div>
<!--Start Attorney's block-->
<div id="attorneyBlock">
    <!--Start Attorney's block-->

<!--end Attorney's block--></div>
<!--end Attorney's block-->
   
	<div class="patentsSummaryBox clearfix">
        <div class="patentsSummaryTitle clearfix">
            <h3>Cause</h3>
        </div>
        <div class="patentsSummaryTxt clearfix">
            <p> 35:271 Patent Infringement</p>
        </div>
    </div>


<div class="patentsSummaryBox clearfix">
        <div class="patentsSummaryTitle clearfix">
        <h3>Related Patents</h3>
    </div>
    <div class='patentsListHolder'>
                
    	<table cellpadding="0" cellspacing="0" class="adminTable" width="100%">
		<tr class="header">
		    		        <th width="90">
		            <span class="sortBy cursorPointer" rel="docNumber">
    				    Doc No    				</span>
		        </th>
		    		        <th width="350">
		            <span class="sortBy cursorPointer" rel="title">
    				    Title    				</span>
		        </th>
		    		        <th >
		            <span class="sortBy cursorPointer" rel="date">
    				    Issue date    				</span>
		        </th>
		    		</tr>
					<tr class="row0">
					<td valign="top">
						06359016					</td>
					<td valign="top">
						<a class="bold" href="/us-patents/06359016">
							Topical suspension formulations containing ciprofloxacin and dexamethasone						</a>
					</td>
					<td valign="top">
						Mar 19, 2002					</td>
			</tr>
					<tr class="row1">
					<td valign="top">
						06284804					</td>
					<td valign="top">
						<a class="bold" href="/us-patents/06284804">
							Topical suspension formulations containing ciprofloxacin and dexamethasone						</a>
					</td>
					<td valign="top">
						Sep 4, 2001					</td>
			</tr>
					</table>
    </div>
</div>

</div>
                            </div>

            
            <div style="clear:both"></div>

                        <div id="rightBottomBlockHolder">
                            </div>
        </div>
        <footer>
            <link href="/images/general/favicon.ico" rel="shortcut icon" >
<link href="/css/compiled/applicationd3157f2f0212a80a5d042c127522a2d5.css" media="screen" rel="stylesheet" type="text/css" >
<link href="/images/general/favicon.ico" rel="shortcut icon" >
<!--[if IE]> <link href="/css/ie.css" media="screen" rel="stylesheet" type="text/css" ><![endif]-->        </footer>
        <div style="clear:both"></div>
    </div>
    <div class="bottomModulesHolder">
            </div>
            <footer>
            <div class="clearfix" style="height: 50px; padding: 0; margin: 0; display:block; margin: 0 auto; text-align: center; width: 120px;">
                <a class="social-homepage twitter" href="https://twitter.com/patexia"></a>
                <a class="social-homepage linkedin" href="http://www.linkedin.com/company/patexia"></a>
                <a class="social-homepage gplus" href="http://plus.google.com/+PatexiaIP/"></a>
                <a class="social-homepage facebook" href="https://www.facebook.com/patexia"></a>
            </div>
            <div id="footer" class="pageLayout">
                <!-- <a href="https://www.patexia.com" class="footerLogo" title="Home"></a>  -->
                <div class="footerLeft">&copy; 2010-2015 Patexia Inc. All Rights Reserved. (v.5.37.0)</div >
                <div class="footerRight">
                    		<a href="/about_us.html">About Us</a>	&nbsp;|&nbsp; 		<a id="menu-pressrelease" class="submenu" href="/pressrelease">Press Releases</a>	&nbsp;|&nbsp; 		<a href="/contact_us.html">Contact Us</a>	&nbsp;|&nbsp; 		<a href="/privacy_policy.html">Privacy Policy</a>	&nbsp;|&nbsp; 		<a href="/terms_of_service.html">Terms of Service</a>	&nbsp;|&nbsp; 		<a href="/career.html">Careers</a>	&nbsp;|&nbsp; 		<a href="/blog">Blog</a>	                </div>
                <div class="clear"></div>
                            </div>
        </footer>
    </div>

</body>

<!DOCTYPE note='cached page: 1439234898' html>