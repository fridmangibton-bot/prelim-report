% =====================================================================
%  style/report.cls -- "Creator's Pre-Production Journal"
%  Core design for the preliminary report (LuaLaTeX + polyglossia).
%  Usage (from the project root):  \documentclass{style/report}
%  Rationale: docs/design-decisions.md. Palette mirror: style/palette.json
% =====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{style/report}[2026/11/20 Pre-Production Journal class]

% Hebrew rule 11.1: 11-12pt. Oneside + openany => no blank pages.
\PassOptionsToClass{12pt,a4paper,oneside,openany}{report}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{report}}
\ProcessOptions\relax
% LaTeX registers "style/report" under the basename "report", which would
% make \LoadClass skip the standard class. Clear that marker first.
\expandafter\let\csname ver@report.cls\endcsname\relax
\LoadClass{report}

% ---------------------------------------------------------------------
% 1. Palette (keep in sync with style/palette.json)
% ---------------------------------------------------------------------
\RequirePackage[table]{xcolor}
\definecolor{paper}{HTML}{F8F3E8}
\definecolor{ink}{HTML}{1E1B2E}
\definecolor{brandMain}{HTML}{D6336C}
\definecolor{brandAccent}{HTML}{F2C12E}     % backgrounds only, never text
\definecolor{brandHighlight}{HTML}{D9C8F5}
\colorlet{ruleLight}{ink!18!paper}           % thin rules between table rows

% ---------------------------------------------------------------------
% 2. Page geometry: 2.5 cm margins + 0.5 cm binding gutter on the RIGHT
%    (Hebrew book binds on the right). Oneside, so the gutter is fixed.
%    NOTE: with a Hebrew main language LuaTeX lays the page out right-to-
%    left, so geometry's "left" is the PHYSICAL RIGHT edge. left=3.0cm
%    therefore puts the 0.5 cm gutter on the right (checked in the PDF).
% ---------------------------------------------------------------------
\RequirePackage[a4paper,top=2.5cm,bottom=2.5cm,left=3.0cm,right=2.5cm,
  footskip=1.2cm]{geometry}

% ---------------------------------------------------------------------
% 3. Language and fonts
% ---------------------------------------------------------------------
\RequirePackage{fontspec}
\RequirePackage{polyglossia}
\setmainlanguage{hebrew}
\setotherlanguage{english}
% Body: David (Hebrew and Latin). Headings: Arial (Hebrew sans).
\setmainfont{David}[AutoFakeSlant=0.18,Ligatures=TeX]
\setsansfont{Arial}[Ligatures=TeX]
\setmonofont{Consolas}
\newfontfamily\hebrewfont[Script=Hebrew,AutoFakeSlant=0.18,Ligatures=TeX]{David}
\newfontfamily\hebrewfontsf[Script=Hebrew,Ligatures=TeX]{Arial}
\newfontfamily\hebrewfonttt[Script=Hebrew]{Consolas}

% A4: English words are never hyphenated (minima above any word length).
\setlanghyphenmins{english}{50}{50}
% Quotes (biblatex) follow the language of the surrounding text.
\RequirePackage{csquotes}

% ---------------------------------------------------------------------
% 4. Layout rules from booklet table 11.1
% ---------------------------------------------------------------------
\RequirePackage{setspace}
\onehalfspacing                 % 1.5 line spacing; text is justified by default
\emergencystretch=4em           % lets TeX stretch word gaps instead of overflowing the margin (overfull hbox)\setcounter{tocdepth}{3}
\setcounter{secnumdepth}{3}
% Figures, tables and equations are numbered per chapter (report default: 3.2).

% Paper background on every page.
\RequirePackage{pagecolor}
\pagecolor{paper}
\AtBeginDocument{\color{ink}}

% ---------------------------------------------------------------------
% 5. Packages
% ---------------------------------------------------------------------
\RequirePackage{graphicx}
\RequirePackage{booktabs}
\RequirePackage{array}
\RequirePackage{longtable}
\RequirePackage{amsmath}
\RequirePackage{tikz}
% RTL fix for LuaTeX: in a right-to-left paragraph every pgf picture (TikZ,
% tcolorbox frames) is drawn mirrored/shifted. Build each picture in a
% left-to-right box, and typeset node text right-to-left again.
\let\journal@pgfpicture\pgfpicture
\let\journal@endpgfpicture\endpgfpicture
\def\pgfpicture{\leavevmode\hbox dir TLT\bgroup\journal@pgfpicture}
\def\endpgfpicture{\journal@endpgfpicture\egroup}
\tikzset{every node/.append style={execute at begin node={\textdir TRT}}}
\RequirePackage[most]{tcolorbox}
\RequirePackage{titlesec}
\RequirePackage{caption}
\RequirePackage[hidelinks]{hyperref}

\newcommand\journal@heading{\sffamily\bfseries\color{ink}}
\newcommand\journal@totalchapters{8}
\newif\ifjournal@inrefs       % true in the references: footer shows "מקורות"
\journal@inrefsfalse
\newcommand\setchaptertotal[1]{\renewcommand\journal@totalchapters{#1}}

% ---------------------------------------------------------------------
% 6. Chapter opener: ink panel with scalloped bottom, <= 1/3 page.
%    Text continues on the same page. TOC keeps the plain title.
% ---------------------------------------------------------------------
\newlength\journal@panelh   \setlength\journal@panelh{7cm}  % + 0.3cm scallops
\newlength\journal@scallop  \setlength\journal@scallop{0.3cm}

% #1 = number line (empty for starred chapters), #2 = pill text, #3 = title
\newcommand\journal@panel[3]{%
  \begin{tikzpicture}[remember picture,overlay]
    \coordinate (PT) at (current page.north west);
    \fill[ink] (PT) rectangle ([yshift=-\journal@panelh]current page.north east);
    \foreach \i in {0,...,40}{%
      \fill[ink] ([xshift=\i*2*\journal@scallop+\journal@scallop,
                   yshift=-\journal@panelh]PT) circle[radius=\journal@scallop];}
    % title block, flush with the right text edge (3.0cm incl. gutter)
    \node[anchor=south east,inner sep=0pt,text width=\textwidth-3.5cm,
          align=right,text=paper,font=\sffamily]
      at ([xshift=-3.0cm,yshift=-\journal@panelh+1.2cm]current page.north east)
      {\ifx\relax#1\relax\else{\large\bfseries #1}\par\vspace{2mm}\fi
       {\fontsize{26}{32}\selectfont\bfseries #3}};
    % SCENE pill on the left text edge
    \ifx\relax#2\relax\else
      \node[anchor=south west,fill=brandMain,text=white,rounded corners=2.6mm,
            inner xsep=3.2mm,inner ysep=1.6mm,font=\sffamily\bfseries\small]
        at ([xshift=2.5cm,yshift=-\journal@panelh+1.2cm]current page.north west)
        {\textenglish{#2}};
    \fi
  \end{tikzpicture}%
}
\newcommand\journal@twodigits[1]{\ifnum#1<10 0\fi\number#1}

\titleformat{\chapter}[block]{}{}{0pt}%
  {\journal@panel{\chaptername\ \thechapter}%
     {SCENE \journal@twodigits{\value{chapter}}}}
\titleformat{name=\chapter,numberless}[block]{}{}{0pt}%
  {\journal@panel{}{}}
% Push the first line of text below the panel (panel bottom ~7.3cm from
% the paper top; the text block starts at 2.5cm).
\titlespacing*{\chapter}{0pt}{-\topskip}{4.6cm}

% ---------------------------------------------------------------------
% 7. Section headings: Hebrew sans in ink + short brandMain underline
% ---------------------------------------------------------------------
% The underline is a zero-size mark at the start (right side) of the
% heading line, drawn 7pt below its baseline, so it never moves the text.
\newcommand\journal@underline{%
  \tikz[overlay]\fill[brandMain] (0,-6pt) rectangle (-1.6cm,-7.6pt);}
\titleformat{\section}{\journal@heading\Large}%
  {\journal@underline\thesection}{0.7em}{}
\titleformat{name=\section,numberless}{\journal@heading\Large}%
  {}{0pt}{\journal@underline}
\titleformat{\subsection}{\journal@heading\large}{\thesubsection}{0.7em}{}
\titleformat{\subsubsection}{\journal@heading\normalsize}{\thesubsubsection}{0.7em}{}
\titlespacing*{\section}{0pt}{3.2ex plus 1ex minus .2ex}{1.4ex plus .2ex}
\titlespacing*{\subsection}{0pt}{2.6ex plus 1ex minus .2ex}{1ex plus .2ex}
\titlespacing*{\subsubsection}{0pt}{2ex plus .5ex minus .2ex}{.6ex plus .2ex}

% ---------------------------------------------------------------------
% 8. Captions: figures below, tables above (write \caption first in a table)
% ---------------------------------------------------------------------
\captionsetup{font={small,stretch=1.15},labelfont={sf,bf},labelsep=colon}
\captionsetup[figure]{position=below,skip=6pt}
\captionsetup[table]{position=above,skip=6pt}

% ---------------------------------------------------------------------
% 9. Tables: ink header row with cream text, thin light rule between rows
%    \headrow  \hcell{A} & \hcell{B} \\   ...   row \\ \rowrule  row \\
% ---------------------------------------------------------------------
\renewcommand\arraystretch{1.25}
% A2: tabular builds its \halign inside math ($\vcenter), and LuaTeX math
% follows \mathdir, which is LTR. Make it RTL inside tables only, so the
% first column is on the right. TikZ pictures keep their own LTR box (INC-003).
\let\journal@tabular\tabular
\renewcommand\tabular{\mathdir TRT\textdir TRT\journal@tabular}
\newcommand\headrow{\rowcolor{ink}}
\newcommand\hcell[1]{{\color{paper}\sffamily\bfseries #1}}
\newcommand\rowrule{\arrayrulecolor{ruleLight}\hline\arrayrulecolor{ink}}

% ---------------------------------------------------------------------
% 10. Boxes
%     directornote = "in our project" post-it (brandAccent, ink text)
%     notebox      = general note (brandHighlight, ink text)
% ---------------------------------------------------------------------
\newtcolorbox{directornote}[1][]{enhanced jigsaw,breakable,
  colback=brandAccent,colframe=brandAccent,coltext=ink,
  colbacktitle=brandAccent,coltitle=ink,titlerule=0pt,
  title={הערת במאי},fonttitle=\sffamily\bfseries,
  sharp corners,boxrule=0pt,left=4mm,right=4mm,top=1mm,bottom=3mm,
  before skip=10pt,after skip=10pt,
  drop fuzzy shadow=ink!35,
  % strip of "tape" holding the note
  overlay unbroken and first={%
    \fill[paper,opacity=.75,rotate around={-3:(frame.north)}]
      ([xshift=-1.4cm,yshift=-1.5mm]frame.north) rectangle
      ([xshift=1.4cm,yshift=2.5mm]frame.north);},
  #1}

\newtcolorbox{notebox}[1][]{enhanced jigsaw,breakable,
  colback=brandHighlight,colframe=brandHighlight,coltext=ink,
  arc=2mm,boxrule=0pt,left=4mm,right=4mm,top=2mm,bottom=2mm,
  before skip=10pt,after skip=10pt,
  fonttitle=\sffamily\bfseries,coltitle=ink,colbacktitle=brandHighlight,
  titlerule=0pt,#1}

% ---------------------------------------------------------------------
% 11. Footer: ink film strip, frame-style page number ("12A"),
%     chapter progress X/8 as brandMain segments (body chapters only)
% ---------------------------------------------------------------------
\newcommand\journal@footer{%
  \begin{tikzpicture}[remember picture,overlay]
    \coordinate (FS) at ([yshift=0.9cm]current page.south west);
    \fill[ink] (FS) rectangle ([yshift=1.7cm]current page.south east);
    % sprocket holes
    \foreach \i in {0,...,46}{%
      \fill[paper,rounded corners=0.3mm]
        ([xshift=\i*0.45cm+0.15cm,yshift=0.06cm]FS) rectangle ++(0.18cm,0.1cm);
      \fill[paper,rounded corners=0.3mm]
        ([xshift=\i*0.45cm+0.15cm,yshift=0.64cm]FS) rectangle ++(0.18cm,0.1cm);}
    % frame-style page number
    \node[draw=paper,line width=0.4pt,rounded corners=0.6mm,text=paper,
          font=\sffamily\bfseries\scriptsize,inner xsep=2mm,inner ysep=0.4mm,
          minimum height=3.2mm]
      at ([yshift=1.3cm]current page.south)
      {\textenglish{\thepage\ifnum\value{chapter}>0 A\fi}};
    % chapter progress
    \ifnum\value{chapter}>0
      \node[anchor=east,text=paper,font=\sffamily\scriptsize,inner sep=0pt]
        (PL) at ([xshift=-3.0cm,yshift=1.3cm]current page.south east)
        {\ifjournal@inrefs מקורות\else פרק \textenglish{\number\value{chapter}/\journal@totalchapters}\fi};
      \foreach \k in {1,...,\journal@totalchapters}{%
        \ifnum\k>\value{chapter}
          \fill[paper!25!ink]
            ([xshift=-2mm-\k*4.4mm+0.6mm,yshift=-0.6mm]PL.west) rectangle ++(3.8mm,1.2mm);
        \else
          \fill[brandMain]
            ([xshift=-2mm-\k*4.4mm+0.6mm,yshift=-0.6mm]PL.west) rectangle ++(3.8mm,1.2mm);
        \fi}
    \fi
  \end{tikzpicture}%
}
\def\ps@journal{%
  \let\@oddhead\@empty\let\@evenhead\@empty
  \def\@oddfoot{\journal@footer\hfil}\let\@evenfoot\@oddfoot}
\let\ps@plain\ps@journal        % chapter pages use "plain"
\pagestyle{journal}

\endinput
