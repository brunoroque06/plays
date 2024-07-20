#set text(12.5pt, font: "SF Compact Rounded")
#let mono = "SF Mono"

#align(center, text(2em, weight: 600)[Bruno Roque])
#v(-1.6em)
#align(center, text(1.2em, font: mono)[Software Engineer])
#v(-1.2em)

#let section(title) = {
  text(1.1em, font: mono, weight: 500)[#title]
  v(-0.9em)
  line(length: 100%, stroke: 0.1em)
  v(-0.7em)
}

#section[Info]

#let ungap = { v(-0.6em) }

#let info(img, cnt) = { grid.cell([#box(baseline: 20%, image("icons/" + img, height: 1.2em)); #h(0.4em); #cnt]) }
#grid(
  columns: (50%, 50%),
  row-gutter: 0.4em,
  info("location.svg", "Zürich, Switzerland"),
  info("mobile.svg", link("tel:+41-765-174-226")[(+41) 765 174 226]),
  info("email.svg", link("mailto:brunoroque06@gmail.com")[brunroque06\@gmail.com]),
  info("website.svg", link("https://brunoroque06.github.io")[brunoroque06.github.io]),
  info("github.svg", link("https://github.com/brunoroque06")[github.com/brunoroque06]),
  info("linkedin.svg", link("https://linkedin.com/in/brunoroque06")[linkedin.com/in/brunoroque06]),
)
#ungap

#section[Experience]

#let url(ref, display) = [#link(ref)[#display] #box(baseline: 20%, image("icons/url.svg", height: 1em))]

#let monospace(cnt) = [#text(0.9em, font: mono)[#cnt]]

#let stage(title, entity, entityUrl, city, country, start, end, duration, desc) = {
  v(0%)
  text(1.2em, weight: 600)[#title]
  v(-0.8em)
  let entity = [#entity - #city, #country]
  if (entityUrl != none) { entity = [#url(entityUrl, entity)] }
  let duration = if duration != none [(#duration) ] else []
  [#entity; #h(1fr); #monospace[#duration#start - #end]]
  ungap
  if (desc != none) {
    desc
    ungap
  }
}

#let exps = (
  (
    "Senior Full Stack Engineer",
    "Axpo",
    none,
    "Baden",
    "Switzerland",
    "03.2023",
    "Present",
    none,
    "..."
  ),
  (
    "Senior Software Developer",
    "Raccoon Works",
    none,
    "Zürich",
    "Switzerland",
    "06.2019",
    "12.2022",
    "3 yrs 7 mos",
    "Development of an analytics system for time-series data. It enabled correlation of events across machines in production lines. Technologies: C#, Python, PostgreSQL, Angular, Bazel, Docker, Azure DevOps, Azure (IaC), Pulumi."
  ),
  (
    "Software Developer",
    "Spoud",
    none,
    "Bern",
    "Switzerland",
    "11.2017",
    "05.2019",
    "1 yr 7 mos",
    "Development of a real-time transport layer, and of analytics pipelines, where I introduced testing. Technologies: Java, Apache Flink, Apache Kafka, Elasticsearch, gRPC, Bazel, Docker.",
  ),
  (
    "Software Engineer",
    "Celfinet (Vodafone)",
    none,
    "Glasgow",
    "Scotland",
    "04.2017",
    "08.2017",
    "5 mos",
    "Development of a desktop application to automate the planning of neighbors in cellular networks. Improved the drop call rate in northern areas of the UK by 30%. Technologies: C#, WPF, Microsoft SQL Server.",
  ),
  (
    "Software Engineer R&D",
    "Celfinet",
    none,
    "Lisbon",
    "Portugal",
    "10.2015",
    "03.2017",
    "1 yr 6 mos",
    "Research of geolocation in mobile and IoT networks using radio frequency propagation models. Improved the geolocation error from 280 to 130 meter. Technologies: C#.",
  ),
  (
    "Software Engineer R&D",
    "Instituto Telecomunicações",
    none,
    "Lisbon",
    "Portugal",
    "01.2015",
    "09.2015",
    "9 mos",
    "Software development of video processing algorithms: detection of black frames, black margins, flashes, block effect, removal of subtitles and inpaint. Technologies: C++, OpenCV, Matlab.",
  )
)

#for e in exps.slice(0, 4) {
  stage(..e)
}

#section[Education]
#stage(
  "MSc in Electrical and Computer Engineering",
  "Instituto Superior Técnico",
  "https://tecnico.ulisboa.pt/en/about-tecnico",
  "Lisbon",
  "Portugal",
  "09.2007",
  "12.2014",
  none,
  none
)

#section[Professional Development]

#let dev(disp, u, date) = {
  v(0%)
  [#url(u, disp); #h(1fr); #monospace[#date]]
  ungap
}

#let devs = (
  (
    "Genetic Algorithm, Decision Tree Player, and other side projects",
    "https://github.com/brunoroque06/plays/tree/main/genetic",
    "Present",
  ),
  (
    "Tool to help my wife fill out reports",
    "https://github.com/brunoroque06/plays/tree/main/reportus",
    "Present",
  ),
  (
    "Architecture Clinic, Michael Montgomery, IDesign",
    "https://www.idesign.net/Clinics/Architecture-Clinic",
    "09.2023",
  ),
  (
    "Architect's Master Class, Juval Löwy, IDesign",
    "https://www.idesign.net/Training/Architect-Master-Class",
    "05.2021",
  ),
  (
    "Project Design Master Class, Juval Löwy, IDesign",
    "https://www.idesign.net/Training/Project-Design-Master-Class",
    "03.2020",
  )
)

#for d in devs.slice(0, 4) {
  dev(..d)
}

#let languages() = {
  section[Languages]
  [English - Proficient (C)]
  ungap
  [German - Intermediate (B)]
  ungap
  [Portuguese - Native]
}

#let technologies() = {
  section[Technologies]
  let techs = (
    ".NET (C#)",
    "Python",
    "Angular",
    "PostgreSQL",
    "Shell",
    "Bazel",
    "Docker",
    "Azure DevOps",
    "Azure (IaC)",
    "Pulumi",
  )
  for t in techs {
    box(block(inset: 0.3em, stroke: 0.1em, t))
    h(1fr)
  }
}

#grid(
  columns: (35%, 65%),
  grid.cell(languages()),
  grid.cell(technologies())
)