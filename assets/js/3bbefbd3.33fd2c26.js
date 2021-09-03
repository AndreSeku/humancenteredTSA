"use strict";(self.webpackChunkdocumentation=self.webpackChunkdocumentation||[]).push([[474],{3905:function(e,t,n){n.d(t,{Zo:function(){return u},kt:function(){return m}});var i=n(7294);function r(e,t,n){return t in e?Object.defineProperty(e,t,{value:n,enumerable:!0,configurable:!0,writable:!0}):e[t]=n,e}function a(e,t){var n=Object.keys(e);if(Object.getOwnPropertySymbols){var i=Object.getOwnPropertySymbols(e);t&&(i=i.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),n.push.apply(n,i)}return n}function o(e){for(var t=1;t<arguments.length;t++){var n=null!=arguments[t]?arguments[t]:{};t%2?a(Object(n),!0).forEach((function(t){r(e,t,n[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(n)):a(Object(n)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(n,t))}))}return e}function l(e,t){if(null==e)return{};var n,i,r=function(e,t){if(null==e)return{};var n,i,r={},a=Object.keys(e);for(i=0;i<a.length;i++)n=a[i],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(i=0;i<a.length;i++)n=a[i],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var p=i.createContext({}),d=function(e){var t=i.useContext(p),n=t;return e&&(n="function"==typeof e?e(t):o(o({},t),e)),n},u=function(e){var t=d(e.components);return i.createElement(p.Provider,{value:t},e.children)},c={inlineCode:"code",wrapper:function(e){var t=e.children;return i.createElement(i.Fragment,{},t)}},s=i.forwardRef((function(e,t){var n=e.components,r=e.mdxType,a=e.originalType,p=e.parentName,u=l(e,["components","mdxType","originalType","parentName"]),s=d(n),m=r,h=s["".concat(p,".").concat(m)]||s[m]||c[m]||a;return n?i.createElement(h,o(o({ref:t},u),{},{components:n})):i.createElement(h,o({ref:t},u))}));function m(e,t){var n=arguments,r=t&&t.mdxType;if("string"==typeof e||r){var a=n.length,o=new Array(a);o[0]=s;var l={};for(var p in t)hasOwnProperty.call(t,p)&&(l[p]=t[p]);l.originalType=e,l.mdxType="string"==typeof e?e:r,o[1]=l;for(var d=2;d<a;d++)o[d]=n[d];return i.createElement.apply(null,o)}return i.createElement.apply(null,n)}s.displayName="MDXCreateElement"},5494:function(e,t,n){n.r(t),n.d(t,{frontMatter:function(){return l},contentTitle:function(){return p},metadata:function(){return d},toc:function(){return u},default:function(){return s}});var i=n(7462),r=n(3366),a=(n(7294),n(3905)),o=["components"],l={sidebar_position:3},p="Pipeline",d={unversionedId:"pipeline",id:"pipeline",isDocsHomePage:!1,title:"Pipeline",description:"The core of the hctsa-package is the pipeline.",source:"@site/docs/pipeline.md",sourceDirName:".",slug:"/pipeline",permalink:"/humancenteredTSA/docs/pipeline",editUrl:"https://github.com/AndreSeku/humancenteredTSA/tree/documentation/docs/pipeline.md",version:"current",sidebarPosition:3,frontMatter:{sidebar_position:3},sidebar:"tutorialSidebar",previous:{title:"Installation",permalink:"/humancenteredTSA/docs/installation"},next:{title:"Method categories",permalink:"/humancenteredTSA/docs/methods/method-categories"}},u=[{value:"Initialize",id:"initialize",children:[]},{value:"Build",id:"build",children:[]},{value:"Run",id:"run",children:[]}],c={toc:u};function s(e){var t=e.components,n=(0,r.Z)(e,o);return(0,a.kt)("wrapper",(0,i.Z)({},c,n,{components:t,mdxType:"MDXLayout"}),(0,a.kt)("h1",{id:"pipeline"},"Pipeline"),(0,a.kt)("p",null,"The core of the ",(0,a.kt)("inlineCode",{parentName:"p"},"hctsa"),"-package is the ",(0,a.kt)("strong",{parentName:"p"},"pipeline"),"."),(0,a.kt)("h2",{id:"initialize"},"Initialize"),(0,a.kt)("p",null,"(1) At first, you need to import the ",(0,a.kt)("strong",{parentName:"p"},"Pipeline"),"-Class, and additionally pandas:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"from hctsa.pipeline.pipeline import Pipeline\nimport pandas as pd\n")),(0,a.kt)("p",null,"(2a) Then you can initialize your specific pipeline with your own data or csv-file:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"data = pd.read_csv('./test_data/testdata.csv', squeeze=True)\npline = Pipeline(series=data)\n")),(0,a.kt)("p",null,"(2b) You can also initialize the pipeline without any data and add the data later:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"pline = Pipeline()\npline.load_data_csv(filename='./test_data/testdata.csv')\n")),(0,a.kt)("p",null,"In both ways, the data is set as the core data, all further methods are based on."),(0,a.kt)("h2",{id:"build"},"Build"),(0,a.kt)("p",null,"To build up the pipeline, the pipeline-method ",(0,a.kt)("inlineCode",{parentName:"p"},"add_method")," can be used, to add another method into the sequence of methods of the pipeline:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"pline.add_method(METHOD_NAME)\n")),(0,a.kt)("p",null,"Where ",(0,a.kt)("inlineCode",{parentName:"p"},"METHOD_NAME")," is the String of the specfic method to be added. There is a number of different methods with individual rules. Hence, just those methods get added into the pipeline, which are allowed dependent on the parent method."),(0,a.kt)("p",null,"So, sequentially adding a number of methods into the pipeline:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"# Example of adding a number of preparation methods:\npline.add_method('point_slope_transformation')\npline.add_method('zscore')\npline.add_method('rolling_mean')\n# Adding an output method for visualization:\npline.add_method('sns_line_plot_series')\n")),(0,a.kt)("h2",{id:"run"},"Run"),(0,a.kt)("p",null,"For running the pipeline and generating an output or result, just use the ",(0,a.kt)("inlineCode",{parentName:"p"},"run"),"-method of the pipeline-class:"),(0,a.kt)("pre",null,(0,a.kt)("code",{parentName:"pre",className:"language-python"},"pline.run()\n")))}s.isMDXComponent=!0}}]);