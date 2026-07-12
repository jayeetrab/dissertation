# Scoring Pack — Multi-city stratified sample (2/city, seed=42)

---

## BIR-SC-01 — BASELINE

**City:** birmingham | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy PG3 of the Birmingham Development Plan 2031 means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy PG3 — source: `Birmingham_Development_Plan_2031.pdf`

### Output (baseline)

**Summary of Policy PG3: Design of New Development in Birmingham**

Dear Residents,

As part of the Birmingham Development Plan 2031, Policy PG3 focuses on the importance of high-quality design in new developments across our city. This policy aims to ensure that any new buildings or changes to existing structures contribute positively to the character and identity of our neighbourhoods. Here’s what this means for you and your community:

1. **High-Quality Design**: New developments must be well-designed, taking into account the local context. This means that buildings should fit in with the surrounding area, respecting the existing architecture and landscape. Developers are encouraged to create designs that enhance the visual appeal of our neighbourhoods.

2. **Sustainability**: Policy PG3 emphasizes sustainable design practices. This includes using materials and construction methods that are environmentally friendly, as well as incorporating features that reduce energy consumption. The aim is to create buildings that are not only beautiful but also efficient and sustainable for the long term.

3. **Community and Accessibility**: The policy highlights the need for developments to be inclusive and accessible to everyone. This means considering how people of all ages and abilities can use and enjoy the spaces created. Developments should promote social interaction and community cohesion, making our neighbourhoods welcoming for all.

4. **Public Spaces**: New developments should also consider the creation and enhancement of public spaces. This includes parks, squares, and other communal areas that can be enjoyed by residents. The design should encourage outdoor activities and provide spaces for social gatherings.

5. **Local Identity**: Policy PG3 encourages developers to reflect the unique character of Birmingham and its diverse communities in their designs. This means that new buildings should celebrate local heritage and culture, contributing to a sense of place that residents can be proud of.

6. **Consultation and Engagement**: The policy supports the idea that local residents should have a say in the design of new developments. Developers are encouraged to engage with the community early in the planning process to gather feedback and ensure that the designs meet the needs and aspirations of local people.

In summary, Policy PG3 is about ensuring that new developments in Birmingham are not only functional but also enhance the quality of life for residents. It aims to create beautiful, sustainable, and inclusive spaces that reflect our community’s identity and values. As residents, your input is vital in shaping the future of our neighbourhoods, and we encourage you to stay engaged in the planning process.

Thank you for your attention, and we look forward to working together to create a vibrant and thriving Birmingham.

Best regards,

[Your Name]  
[Your Position]  
[Your Contact Information]  
[Date]

### Rubric (enter in the Evaluate page for `BIR-SC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## BIR-SC-01 — RAG

**City:** birmingham | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy PG3 of the Birmingham Development Plan 2031 means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy PG3 — source: `Birmingham_Development_Plan_2031.pdf`

### Output (rag)

**Summary of Policy PG3: Place-making in the Birmingham Development Plan 2031**

Policy PG3 of the Birmingham Development Plan 2031 focuses on the concept of "place-making," which is about creating attractive, functional, and sustainable environments for residents and visitors. Here’s what this means for the design of new developments in your neighbourhood:

1. **High-Quality Design**: New developments will be expected to be well-designed and visually appealing. This means that buildings should not only look good but also fit in with the character of the area. The aim is to enhance the overall aesthetic of the neighbourhood, making it a more pleasant place to live and visit.

2. **Sustainable Neighbourhoods**: The policy emphasizes the importance of sustainability. This includes using materials and construction methods that are environmentally friendly, as well as ensuring that developments are energy-efficient. The goal is to create neighbourhoods that are not only beautiful but also contribute positively to the environment (Birmingham Development Plan, Page 20).

3. **Accessibility and Connectivity**: New developments should ensure that local jobs and services are easily accessible. This means that there should be good transport links and pathways that allow residents to move around easily, whether by walking, cycling, or using public transport. The aim is to reduce reliance on cars and promote healthier, more active lifestyles (Birmingham Development Plan, Page 20).

4. **Community Focus**: The policy encourages developments that foster a sense of community. This could involve creating public spaces, parks, and community facilities that encourage social interaction among residents. The idea is to build neighbourhoods where people feel connected and engaged with one another.

5. **Meeting Local Needs**: The design of new developments should take into account the needs of the local population, including the provision of affordable housing. This ensures that everyone in the community can find suitable accommodation and that the neighbourhood remains inclusive (Birmingham Development Plan, Page 20).

In summary, Policy PG3 aims to create neighbourhoods that are not only functional and sustainable but also vibrant and welcoming. By focusing on high-quality design, accessibility, community engagement, and local needs, the policy seeks to enhance the quality of life for all residents in Birmingham.

### Retrieved context (8 chunks — verify citations against these)

**[1] Birmingham_Development_Plan_2031.pdf p.3 (city: birmingham, score 0.744)**
> contents / birmingham development plan
Contents
Foreword                 5
1  Introduction               7
2  About Birmingham              11 
  3  The vision, objectives and strategy           17
The vision - Birmingham in 2031 
Objectives 
The strategy
  4  Planning for growth            27
PG1   Overall levels of growth
PG2   Birmingham as an international city 
PG3   Place making 
 
  5  Spat

**[2] Birmingham_Development_Plan_2031.pdf p.3 (city: birmingham, score 0.744)**
> contents / birmingham development plan
Contents
Foreword                 5
1  Introduction               7
2  About Birmingham              11 
  3  The vision, objectives and strategy           17
The vision - Birmingham in 2031 
Objectives 
The strategy
  4  Planning for growth            27
PG1   Overall levels of growth
PG2   Birmingham as an international city 
PG3   Place making 
 
  5  Spat

**[3] Birmingham_Development_Plan_2031.pdf p.147 (city: birmingham, score 0.7347)**
> monitoring / birmingham development plan
145
PG1 Overall Levels of Growth
PG2  Birmingham as an 
International City
PG3 Place-making
GA1-GA10 Growth Areas
TP1  Reducing the City’s Carbon 
Footprint
TP2 Adapting to Climate Change
TP3 Sustainable Construction
TP4  Low and Zero Carbon Energy 
Generation
•  Net/gross dwelling completions in the City Council area.
•  Net/gross dwelling completions in o

**[4] Birmingham_Development_Plan_2031.pdf p.147 (city: birmingham, score 0.7347)**
> monitoring / birmingham development plan
145
PG1 Overall Levels of Growth
PG2  Birmingham as an 
International City
PG3 Place-making
GA1-GA10 Growth Areas
TP1  Reducing the City’s Carbon 
Footprint
TP2 Adapting to Climate Change
TP3 Sustainable Construction
TP4  Low and Zero Carbon Energy 
Generation
•  Net/gross dwelling completions in the City Council area.
•  Net/gross dwelling completions in o

**[5] Birmingham_Development_Plan_2031.pdf p.20 (city: birmingham, score 0.7299)**
> 18
birmingham development plan / the vision, objectives and strategy
3.2 We will plan to ensure 
Birmingham’s residents will be 
experiencing a high quality 
of life, living within attractive 
and well designed sustainable 
neighbourhoods. The choice and 
affordability of housing will be 
meeting the needs of all and local 
jobs and services will be accessible 
by a range of sustainable transport 

**[6] Birmingham_Development_Plan_2031.pdf p.20 (city: birmingham, score 0.7297)**
> 18
birmingham development plan / the vision, objectives and strategy
3.2 We will plan to ensure 
Birmingham’s residents will be 
experiencing a high quality 
of life, living within attractive 
and well designed sustainable 
neighbourhoods. The choice and 
affordability of housing will be 
meeting the needs of all and local 
jobs and services will be accessible 
by a range of sustainable transport 

**[7] Birmingham_Development_Plan_2031.pdf p.32 (city: birmingham, score 0.7208)**
> Birmingham will be promoted as an international city supporting 
development, investment and other initiatives that raise the City’s profile 
and strengthen its position nationally and internationally.
Implementation
Policy PG2          3            3           3       3             3                   3
Local/
National 
Funding
Partnerships CPO CIL/
Section 
106
Other Local Plan/
SPD/Regeneration

**[8] Birmingham_Development_Plan_2031.pdf p.32 (city: birmingham, score 0.7208)**
> Birmingham will be promoted as an international city supporting 
development, investment and other initiatives that raise the City’s profile 
and strengthen its position nationally and internationally.
Implementation
Policy PG2          3            3           3       3             3                   3
Local/
National 
Funding
Partnerships CPO CIL/
Section 
106
Other Local Plan/
SPD/Regeneration

### Rubric (enter in the Evaluate page for `BIR-SC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## BIR-PC-01 — BASELINE

**City:** birmingham | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Birmingham city centre comply with the housing policies of the Birmingham Development Plan 2031 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy PG1, Policy TP27, Policy TP30, NPPF para 11, NPPF para 120 — source: `Birmingham_Development_Plan_2031.pdf`

### Output (baseline)

To assess whether the proposed 80-unit residential development on a brownfield site in Birmingham city centre complies with the housing policies of the Birmingham Development Plan 2031 and the National Planning Policy Framework (NPPF) December 2024, we need to consider several key policies and principles from both documents.

### Birmingham Development Plan 2031

1. **Policy TP1: Sustainable Transport** - This policy emphasizes the importance of sustainable transport options in new developments. Given the city centre location, the development is likely to benefit from good public transport links, which aligns with this policy.

2. **Policy PG1: Overall Development Strategy** - This policy supports the efficient use of land, particularly on brownfield sites. The proposed development on a brownfield site is consistent with the aim of maximizing the use of previously developed land, which is a priority in urban areas.

3. **Policy H1: Housing Requirement** - The Birmingham Development Plan sets out a requirement for new housing to meet the needs of the city. The proposed 80 units would contribute to the overall housing supply, which is crucial given Birmingham's identified housing need.

4. **Policy H2: Housing Mix** - This policy encourages a mix of housing types and sizes to meet diverse needs. The proposal should demonstrate how it addresses this requirement, potentially through a mix of unit sizes or types (e.g., affordable housing, family units).

5. **Policy H3: Affordable Housing** - The plan requires a percentage of new housing to be affordable. The developer must ensure that the proposal includes an appropriate level of affordable housing, in line with local needs and policy requirements.

### National Planning Policy Framework (NPPF) December 2024

1. **Paragraph 11** - This paragraph establishes the presumption in favour of sustainable development. The proposed development on a brownfield site in a city centre location is likely to be considered sustainable, particularly if it meets local housing needs.

2. **Paragraph 60** - This paragraph emphasizes the need for local planning authorities to assess and meet the housing needs of their area. The proposed development should align with Birmingham's identified housing needs, contributing to the overall supply.

3. **Paragraph 68** - This paragraph encourages the development of small and medium-sized sites to meet housing needs. An 80-unit development can be considered a medium-sized site, which is supported by national policy.

4. **Paragraph 74** - This paragraph highlights the importance of delivering a sufficient supply of homes. The proposed development should contribute to the five-year housing land supply, which is critical for local authorities to maintain.

5. **Paragraph 92** - This paragraph promotes the creation of inclusive and safe places that promote health and well-being. The design and layout of the proposed development should consider these aspects to ensure it meets community needs.

### Conclusion

In summary, the proposed 80-unit residential development on a brownfield site in Birmingham city centre appears to comply with both the Birmingham Development Plan 2031 and the NPPF December 2024. Key policies that support this conclusion include:

- **Birmingham Development Plan**: Policies TP1, PG1, H1, H2, and H3.
- **NPPF**: Paragraphs 11, 60, 68, 74, and 92.

However, it is essential for the developer to provide detailed information on how the proposal meets the specific requirements of affordable housing, housing mix, and sustainable transport to ensure full compliance with local and national policies. Additionally, engagement with local stakeholders and consideration of any potential impacts on the surrounding area will be crucial in the planning process.

### Rubric (enter in the Evaluate page for `BIR-PC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## BIR-PC-01 — RAG

**City:** birmingham | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Birmingham city centre comply with the housing policies of the Birmingham Development Plan 2031 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy PG1, Policy TP27, Policy TP30, NPPF para 11, NPPF para 120 — source: `Birmingham_Development_Plan_2031.pdf`

### Output (rag)

The proposed 80-unit residential development on a brownfield site in Birmingham city centre aligns well with the housing policies outlined in the Birmingham Development Plan 2031 and the National Planning Policy Framework (NPPF) December 2024.

1. **Birmingham Development Plan 2031**:
   - **Policy TP28**: This policy emphasizes the importance of locating new housing on previously developed land within the existing urban area. The context explicitly states that the City Council expects a minimum of 80% of new homes to be built on previously developed land to meet the needs of Birmingham’s growing population (Extract 1). Since the proposed development is on a brownfield site, it directly complies with this policy.
   - **Urban Regeneration and Economic Revitalisation**: The plan aims to ensure that residents can live in comfortable and affordable homes in sustainable neighbourhoods (Extract 5). The development of 80 units on a brownfield site contributes to urban regeneration, which is a key objective of the plan.

2. **National Planning Policy Framework (NPPF)**:
   - While the specific paragraphs from the NPPF are not provided in the context, it is known that the NPPF encourages the use of brownfield land for housing development as part of its commitment to sustainable development. The NPPF requires local authorities to promote the effective use of land by reusing land that has been previously developed (NPPF paragraph 117). Therefore, the proposed development is consistent with the NPPF's objectives.

In summary, the proposed 80-unit residential development on a brownfield site in Birmingham city centre complies with both the Birmingham Development Plan 2031 (specifically Policy TP28) and the overarching principles of the NPPF regarding the use of previously developed land for housing. This development supports the city's goals for urban regeneration and meets the requirements for sustainable housing development.

### Retrieved context (8 chunks — verify citations against these)

**[1] Birmingham_Development_Plan_2031.pdf p.111 (city: birmingham, score 0.7519)**
> located on previously developed 
land within the existing urban 
area. Based on an assessment of 
future land supply, the City Council 
expects that a minimum of 80% 
of new homes provided in the city  
over the plan period will be built 
on previously developed land. As 
set out in Section 3 it has been 
necessary, in order to meet the 
needs of Birmingham’s growing 
population, to identify some 

**[2] Birmingham_Development_Plan_2031.pdf p.111 (city: birmingham, score 0.7518)**
> located on previously developed 
land within the existing urban 
area. Based on an assessment of 
future land supply, the City Council 
expects that a minimum of 80% 
of new homes provided in the city  
over the plan period will be built 
on previously developed land. As 
set out in Section 3 it has been 
necessary, in order to meet the 
needs of Birmingham’s growing 
population, to identify some 

**[3] Birmingham_Development_Plan_2031.pdf p.121 (city: birmingham, score 0.7491)**
> •  Promoting safe residential environments and addressing the fear of 
crime.
•  Improving road safety (Policy TP39 and Policy TP44).
•  Addressing climate change issues.
•  Making provision for open space and allotments (policy TP9).
Proposals for the development of new and the improvement of existing 
health care infrastructure required to support Birmingham’s growing 
population will be permitt

**[4] Birmingham_Development_Plan_2031.pdf p.121 (city: birmingham, score 0.7491)**
> •  Promoting safe residential environments and addressing the fear of 
crime.
•  Improving road safety (Policy TP39 and Policy TP44).
•  Addressing climate change issues.
•  Making provision for open space and allotments (policy TP9).
Proposals for the development of new and the improvement of existing 
health care infrastructure required to support Birmingham’s growing 
population will be permitt

**[5] Birmingham_Development_Plan_2031.pdf p.110 (city: birmingham, score 0.7479)**
> 108
birmingham development plan / homes and neighbourhoods
8.2 The following policies 
contribute to the strategy for 
urban regeneration and economic 
revitalisation by ensuring that 
Birmingham’s residents can live in 
comfortable and affordable homes 
in sustainable and successful 
neighbourhoods. The approach 
will need to ensure that there is 
sufficient land available to enable 
a variety of

**[6] Birmingham_Development_Plan_2031.pdf p.110 (city: birmingham, score 0.7479)**
> 108
birmingham development plan / homes and neighbourhoods
8.2 The following policies 
contribute to the strategy for 
urban regeneration and economic 
revitalisation by ensuring that 
Birmingham’s residents can live in 
comfortable and affordable homes 
in sustainable and successful 
neighbourhoods. The approach 
will need to ensure that there is 
sufficient land available to enable 
a variety of

**[7] Nottingham_LAPP_2020.pdf p.194 (city: nottingham, score 0.6179)**
> Section 6: Development Management Policies – Making it Happen 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 186 
 
 
 
Justification 
 
Housing 
 
6.13  The NPPF requires local authorities to identify annually a supply of specific deliverable 

**[8] Nottingham_LAPP_2020.pdf p.194 (city: nottingham, score 0.6179)**
> Section 6: Development Management Policies – Making it Happen 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 186 
 
 
 
Justification 
 
Housing 
 
6.13  The NPPF requires local authorities to identify annually a supply of specific deliverable 

### Rubric (enter in the Evaluate page for `BIR-PC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEE-ST-02 — BASELINE

**City:** leeds | **Category:** strategic_analysis | **Difficulty:** medium

**Task:** What affordable housing percentage and site-size threshold applies to major residential developments in Leeds, and which local plan policy sets this? Answer for Leeds specifically.

**Expected policies (check these in the source PDF):** Policy H5 — source: `Leeds_Core_Strategy_2019_consolidated.pdf`

### Output (baseline)

In Leeds, the provision of affordable housing for major residential developments is governed by the Leeds Core Strategy, specifically Policy H5. According to this policy, the affordable housing requirement is set at a percentage of the total number of dwellings proposed in a development.

For major residential developments in Leeds, which are defined as those comprising 10 or more dwellings or sites of 0.5 hectares or more, the affordable housing requirement is typically 15% of the total units. This percentage applies across the majority of the city, although it may vary in certain areas or under specific circumstances, such as in designated areas of high need or where viability assessments indicate a different percentage can be supported.

The Core Strategy also emphasizes the importance of delivering affordable housing to meet local needs, aligning with the National Planning Policy Framework (NPPF) which encourages local authorities to plan for a mix of housing, including affordable housing, to meet the needs of different groups in the community (NPPF, Paragraph 61).

In summary, for major residential developments in Leeds, the affordable housing requirement is 15%, as set out in Policy H5 of the Leeds Core Strategy, applicable to developments of 10 or more dwellings or sites of 0.5 hectares or larger.

### Rubric (enter in the Evaluate page for `LEE-ST-02` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEE-ST-02 — RAG

**City:** leeds | **Category:** strategic_analysis | **Difficulty:** medium

**Task:** What affordable housing percentage and site-size threshold applies to major residential developments in Leeds, and which local plan policy sets this? Answer for Leeds specifically.

**Expected policies (check these in the source PDF):** Policy H5 — source: `Leeds_Core_Strategy_2019_consolidated.pdf`

### Output (rag)

In Leeds, the requirement for affordable housing in major residential developments is informed by the Leeds Core Strategy, specifically under the affordable housing section. According to the context provided, the Core Strategy indicates that for "Build to Rent" developments, developers can either provide affordable housing on-site or pay a commuted sum in lieu of on-site provision. The consultation currently suggests that 20% of total dwellings should be designated as “Affordable Private Rent” (Extract 5).

However, the specific percentage of affordable housing required for major residential developments, as well as the site-size threshold that triggers this requirement, is not explicitly detailed in the extracts provided. Typically, in many local plans, a threshold of 10 or more dwellings is common for major developments, but this specific detail is not included in the context.

The relevant local plan policy that sets these requirements is the Leeds Core Strategy, particularly the sections on affordable housing (Extracts 1, 5, and 6). The Core Strategy emphasizes the need for affordable housing to meet local needs as identified in the Leeds Strategic Housing Market Assessment (SHMA 2017), which indicates an annual need of 1,230 affordable housing dwellings across Leeds (Extract 1).

In summary, while the Core Strategy specifies a 20% affordable housing requirement for Build to Rent developments, the exact percentage and site-size threshold for all major residential developments in Leeds are not explicitly stated in the provided extracts. Further details may be found in other sections of the Core Strategy or supplementary planning documents.

### Retrieved context (8 chunks — verify citations against these)

**[1] Leeds_Core_Strategy_2019_consolidated.pdf p.90 (city: leeds, score 0.8012)**
> Affordable Housing  
5.2.12 In conformity with national planning guidance, affordable housing will be required to meet 
local needs informed by the Leeds Strategic Housing Market Assessment (SHMA 2017) 
and the Economic Viability Study 2017. 
 
5.2.13 The Strategic Housing Market Assessment (2017) identifies an annual need of 1230 
affordable housing dwellings across Leeds. It also suggests that 6

**[2] Leeds_Core_Strategy_2019_consolidated.pdf p.90 (city: leeds, score 0.8012)**
> Affordable Housing  
5.2.12 In conformity with national planning guidance, affordable housing will be required to meet 
local needs informed by the Leeds Strategic Housing Market Assessment (SHMA 2017) 
and the Economic Viability Study 2017. 
 
5.2.13 The Strategic Housing Market Assessment (2017) identifies an annual need of 1230 
affordable housing dwellings across Leeds. It also suggests that 6

**[3] Leeds_Core_Strategy_2019_consolidated.pdf p.88 (city: leeds, score 0.7787)**
> the Leeds Main Urban Area as well as Major Settlements, and ‘Smaller Settlements’ and 
includes sites within and adjacent  to them . For all other areas, no minimum density  
applies because other housing Policies only allow for a small amount of hous ing 
development in these areas.  The density Policy will apply to all forms of housing 
development, including specialist housing, but not resident

**[4] Leeds_Core_Strategy_2019_consolidated.pdf p.88 (city: leeds, score 0.7787)**
> the Leeds Main Urban Area as well as Major Settlements, and ‘Smaller Settlements’ and 
includes sites within and adjacent  to them . For all other areas, no minimum density  
applies because other housing Policies only allow for a small amount of hous ing 
development in these areas.  The density Policy will apply to all forms of housing 
development, including specialist housing, but not resident

**[5] Leeds_Core_Strategy_2019_consolidated.pdf p.90 (city: leeds, score 0.7777)**
> the flats. 
 
5.2.16 Build to rent developments in Leeds can either provide affordable housing on- site as 
advised in national guidance or in line with the first paragraphs of Policy H5. If developers 
prefer to pay a commuted sum in lieu of on-site provision, this should be calculated on 
the basis of paragraph  5.2.17.4. Regarding requirements in national guidance, 
consultation currently sugge

**[6] Leeds_Core_Strategy_2019_consolidated.pdf p.90 (city: leeds, score 0.7777)**
> the flats. 
 
5.2.16 Build to rent developments in Leeds can either provide affordable housing on- site as 
advised in national guidance or in line with the first paragraphs of Policy H5. If developers 
prefer to pay a commuted sum in lieu of on-site provision, this should be calculated on 
the basis of paragraph  5.2.17.4. Regarding requirements in national guidance, 
consultation currently sugge

**[7] Leeds_Core_Strategy_2019_consolidated.pdf p.88 (city: leeds, score 0.7691)**
> Housing Density 
5.2.9 A minimum density Policy is needed for Leeds to ensure sustainable housing 
development.  This means efficient use of land in order to avoid more greenfield land 
being developed than is necessary and in order to achieve a higher population in 
proximity to centres.  Lower density schemes will be accepted in exceptional 
circumstances relating to townscape and character.  Ex

**[8] Leeds_Core_Strategy_2019_consolidated.pdf p.88 (city: leeds, score 0.7688)**
> Housing Density 
5.2.9 A minimum density Policy is needed for Leeds to ensure sustainable housing 
development.  This means efficient use of land in order to avoid more greenfield land 
being developed than is necessary and in order to achieve a higher population in 
proximity to centres.  Lower density schemes will be accepted in exceptional 
circumstances relating to townscape and character.  Ex

### Rubric (enter in the Evaluate page for `LEE-ST-02` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEE-SC-01 — BASELINE

**City:** leeds | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy P10 of the Leeds Core Strategy (as amended 2019) means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy P10 — source: `Leeds_Core_Strategy_2019_consolidated.pdf`

### Output (baseline)

**Summary of Policy P10: Design of New Development in Leeds**

Dear Residents,

We want to take a moment to explain what Policy P10 of the Leeds Core Strategy means for the design of new developments in our neighbourhood. This policy is important because it sets out the expectations for how new buildings and spaces should look and function, ensuring they contribute positively to our community.

**Key Points of Policy P10:**

1. **High-Quality Design**: The policy emphasizes that all new developments must be of high quality. This means that buildings should not only be attractive but also well-constructed and durable. The aim is to create spaces that people enjoy using and that stand the test of time.

2. **Contextual Fit**: New developments should respect and enhance the character of the area. This means considering the existing buildings, streets, and landscapes when designing new projects. Developers are encouraged to take cues from local architecture and materials to ensure that new buildings blend in harmoniously with their surroundings.

3. **Sustainability**: Policy P10 promotes sustainable design practices. This includes using energy-efficient materials and technologies, reducing waste, and considering the environmental impact of new developments. The goal is to create buildings that are not only good for the community but also for the planet.

4. **Accessibility and Inclusivity**: The policy highlights the importance of making new developments accessible to everyone, including people with disabilities. This means designing buildings and public spaces that are easy to navigate and use for all members of the community.

5. **Public Spaces**: New developments should include well-designed public spaces that encourage social interaction and community engagement. This could be parks, plazas, or other communal areas where residents can gather and enjoy their neighbourhood.

6. **Safety and Security**: The design of new developments should also consider safety and security. This includes ensuring that buildings are well-lit, visible, and designed to reduce the risk of crime, creating a safe environment for all residents.

7. **Community Involvement**: Finally, the policy encourages developers to engage with local residents during the planning process. This means that your views and concerns should be taken into account when new projects are being proposed, ensuring that developments meet the needs of the community.

In summary, Policy P10 aims to ensure that new developments in Leeds are not only visually appealing but also functional, sustainable, and beneficial to the community. By adhering to these principles, we can create a neighbourhood that we are all proud to be a part of.

If you have any questions or would like to discuss this policy further, please feel free to reach out.

Best regards,

[Your Name]  
[Your Position]  
[Contact Information]  
[Date]

### Rubric (enter in the Evaluate page for `LEE-SC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEE-SC-01 — RAG

**City:** leeds | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy P10 of the Leeds Core Strategy (as amended 2019) means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy P10 — source: `Leeds_Core_Strategy_2019_consolidated.pdf`

### Output (rag)

The provided context does not include specific information about Policy P10 of the Leeds Core Strategy. Therefore, I cannot directly summarize that policy based solely on the extracts given. However, I can provide a general understanding of what policies like P10 typically encompass in the context of urban planning, particularly in relation to design principles.

In general, policies similar to P10 in local planning documents often focus on ensuring that new developments are designed to be high-quality, sustainable, and in keeping with the character of the surrounding area. This can include considerations such as:

1. **Architectural Quality**: New buildings should be well-designed and visually appealing, contributing positively to the local environment.

2. **Contextual Fit**: Developments should respect the scale, form, and materials of existing buildings and the overall character of the neighbourhood.

3. **Sustainability**: New developments are encouraged to incorporate sustainable design practices, such as energy efficiency, use of renewable materials, and green spaces.

4. **Accessibility**: Designs should ensure that buildings and public spaces are accessible to all members of the community, including those with disabilities.

5. **Community Integration**: Developments should enhance community cohesion by providing spaces that encourage social interaction and are accessible to local residents.

While the specific details of Policy P10 are not available in the context provided, these principles are commonly found in urban planning policies aimed at guiding the design of new developments. For precise details on Policy P10, residents should refer to the full Leeds Core Strategy document or consult with local planning authorities.

### Retrieved context (8 chunks — verify citations against these)

**[1] Leeds_Core_Strategy_2019_consolidated.pdf p.1 (city: leeds, score 0.7479)**
> Adopted November 2014
Amendments Adopted 11th September 2019
Core Strategy (as 
amended by the Core 
Strategy Selective 
Review 2019)
Leeds Local Plan

**[2] Leeds_Core_Strategy_2019_consolidated.pdf p.1 (city: leeds, score 0.7479)**
> Adopted November 2014
Amendments Adopted 11th September 2019
Core Strategy (as 
amended by the Core 
Strategy Selective 
Review 2019)
Leeds Local Plan

**[3] Leeds_Core_Strategy_2019_consolidated.pdf p.17 (city: leeds, score 0.7329)**
> for a more child friendly Leeds. These include: travel, the City Centre, places and spaces, 
a healthy lifestyle and jobs. In contributing directly to these wishes and in influencing 
others, the Core Strategy sets out an overall spatial vision, objectives and policy 
framework to improve quality of life across the District, including the lives of children and 
young people.  Leeds is a diverse Ci

**[4] Leeds_Core_Strategy_2019_consolidated.pdf p.17 (city: leeds, score 0.7329)**
> for a more child friendly Leeds. These include: travel, the City Centre, places and spaces, 
a healthy lifestyle and jobs. In contributing directly to these wishes and in influencing 
others, the Core Strategy sets out an overall spatial vision, objectives and policy 
framework to improve quality of life across the District, including the lives of children and 
young people.  Leeds is a diverse Ci

**[5] Leeds_Core_Strategy_2019_consolidated.pdf p.139 (city: leeds, score 0.7307)**
> Green Space  
 
Introduction and Aims 
5.5.9 The overall aim of the Core Strategy green space policies is to use the development 
process through the Local Plan to strategically deliver the best type and the best quality 
of green space to where it is most needed in Leeds. 
 
 Standards (Surplus and Deficiencies)  
5.5.10 Leeds is a City which benefits from good overall provision of green space. H

**[6] Leeds_Core_Strategy_2019_consolidated.pdf p.139 (city: leeds, score 0.7305)**
> Green Space  
 
Introduction and Aims 
5.5.9 The overall aim of the Core Strategy green space policies is to use the development 
process through the Local Plan to strategically deliver the best type and the best quality 
of green space to where it is most needed in Leeds. 
 
 Standards (Surplus and Deficiencies)  
5.5.10 Leeds is a City which benefits from good overall provision of green space. H

**[7] Leeds_Core_Strategy_2019_consolidated.pdf p.167 (city: leeds, score 0.7303)**
> identify
 reasons why progress may be slow.  Monitoring of the Leeds Core Strategy is 
discussed further below. 
 
6.26 Policy ID1 therefore summarises the methods by which the Council will ensure delivery 
and implementation of the Core Strategy. 
                                
  
  
Planning Obligations and the Community Infrastructure Levy 
6.27 The Council reaches decisions on planning appli

**[8] Leeds_Core_Strategy_2019_consolidated.pdf p.167 (city: leeds, score 0.7303)**
> identify
 reasons why progress may be slow.  Monitoring of the Leeds Core Strategy is 
discussed further below. 
 
6.26 Policy ID1 therefore summarises the methods by which the Council will ensure delivery 
and implementation of the Core Strategy. 
                                
  
  
Planning Obligations and the Community Infrastructure Levy 
6.27 The Council reaches decisions on planning appli

### Rubric (enter in the Evaluate page for `LEE-SC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEI-PC-01 — BASELINE

**City:** leicester | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Leicester city centre comply with the housing policies of the Leicester Local Plan 2020-2036 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy SL01, NPPF para 11, NPPF para 120 — source: `Leicester_Local_Plan_2020-2036_Adopted_2026.pdf`

### Output (baseline)

To assess whether the proposed 80-unit residential development on a brownfield site in Leicester city centre complies with the housing policies of the Leicester Local Plan 2020-2036 and the National Planning Policy Framework (NPPF) December 2024, we need to evaluate the proposal against relevant policies and guidance.

### Leicester Local Plan 2020-2036

1. **Policy H1: Housing Requirement**  
   The Leicester Local Plan sets out a housing requirement that must be met to address the city's housing needs. The proposed development of 80 units should contribute positively towards meeting this requirement. The plan emphasizes the need for a mix of housing types and tenures to cater to diverse needs.

2. **Policy H2: Housing Mix**  
   This policy requires developments to provide a mix of housing types and sizes. The proposal should demonstrate how it meets local housing needs, including affordable housing provision. The Local Plan typically specifies a percentage of affordable housing that should be included in developments of this size.

3. **Policy H3: Affordable Housing**  
   The Local Plan outlines the need for affordable housing in new developments. For developments of 15 units or more, a minimum percentage of affordable housing is usually required. The applicant should provide details on how the proposed development will meet this requirement.

4. **Policy H4: Design and Layout of New Housing**  
   This policy emphasizes the importance of high-quality design and layout in residential developments. The proposal should demonstrate that it adheres to principles of good design, including considerations for density, amenity space, and integration with the surrounding area.

5. **Policy DS1: Development Strategy**  
   The Local Plan encourages development on previously developed land (brownfield sites) within the city, particularly in sustainable locations such as the city centre. The proposed site being brownfield aligns with this policy, promoting the efficient use of land.

### National Planning Policy Framework (NPPF) December 2024

1. **Paragraph 11: Presumption in Favour of Sustainable Development**  
   The NPPF promotes a presumption in favour of sustainable development, which is particularly relevant for developments in urban areas. The proposed development should demonstrate that it contributes to sustainable growth, including economic, social, and environmental benefits.

2. **Paragraph 60: Housing Needs**  
   The NPPF emphasizes the need to significantly boost the supply of homes. The proposed development should align with local housing needs assessments and contribute to the overall housing supply in Leicester.

3. **Paragraph 62: Affordable Housing**  
   Similar to the Local Plan, the NPPF highlights the importance of providing affordable housing. The proposal should include a strategy for delivering affordable units in line with local policy requirements.

4. **Paragraph 130: Achieving Well-Designed Places**  
   This paragraph stresses the importance of high-quality design in new developments. The proposal should ensure that it enhances the character of the area and provides a positive contribution to the local environment.

5. **Paragraph 180: Planning for Climate Change**  
   The NPPF encourages developments to mitigate climate change impacts. The proposal should include measures for sustainability, such as energy efficiency and sustainable drainage systems.

### Conclusion

In summary, the proposed 80-unit residential development on a brownfield site in Leicester city centre appears to align with several key policies of the Leicester Local Plan 2020-2036 and the NPPF December 2024. However, compliance will depend on specific details regarding:

- The mix and tenure of housing, particularly affordable housing.
- The design quality and integration with the surrounding area.
- Sustainability measures incorporated into the development.

It is essential for the applicant to provide comprehensive documentation addressing these policies to ensure compliance and support a successful planning application.

### Rubric (enter in the Evaluate page for `LEI-PC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEI-PC-01 — RAG

**City:** leicester | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Leicester city centre comply with the housing policies of the Leicester Local Plan 2020-2036 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy SL01, NPPF para 11, NPPF para 120 — source: `Leicester_Local_Plan_2020-2036_Adopted_2026.pdf`

### Output (rag)

To assess whether the proposed 80-unit residential development on a brownfield site in Leicester city centre complies with the housing policies of the Leicester Local Plan 2020-2036 and the National Planning Policy Framework (NPPF), we can refer to the relevant extracts from the provided context.

1. **Leicester Local Plan Policies**:
   - **Policy SL01: Location of Development**: This policy indicates that development within the Leicester City administrative boundary should align with the spatial strategy outlined in the Local Plan. While the specific details of the spatial strategy are not provided in the extracts, it is essential that the proposed development is consistent with this strategy, which typically prioritizes sustainable development and the efficient use of land, particularly on brownfield sites (Extract 1).
   - **General Development Principles**: The Local Plan states that appropriate proposals can be approved to improve economic, social, and environmental conditions in Leicester (Extract 5). This suggests that if the development meets these criteria, it could be supported.

2. **National Planning Policy Framework (NPPF)**:
   - **Sustainable Development**: The NPPF emphasizes the need for local planning authorities to support sustainable development (NPPF paragraph 8). This includes ensuring that housing developments contribute positively to the economic, social, and environmental objectives of the planning system. The proposed residential development on a brownfield site aligns with this principle, as it promotes the reuse of previously developed land, which is a key aspect of sustainable development.
   - **Housing Supply**: The NPPF requires local authorities to identify a supply of specific deliverable sites sufficient to provide five years’ worth of housing (NPPF paragraph 73). If Leicester City Council has identified a need for new housing and the proposed development contributes to meeting this need, it would further support compliance with NPPF policies.

3. **Conclusion**:
Based on the information provided, the proposed 80-unit residential development on a brownfield site in Leicester city centre appears to comply with the housing policies of the Leicester Local Plan and the NPPF, provided it aligns with the spatial strategy outlined in the Local Plan and contributes positively to the economic, social, and environmental objectives. The reuse of a brownfield site is particularly favorable under both the Local Plan and NPPF, as it supports sustainable development principles.

In summary, the relevant policies are:
- **Leicester Local Plan Policy SL01** (Location of Development)
- **Leicester Local Plan General Development Principles** (improving conditions)
- **NPPF paragraph 8** (sustainable development)
- **NPPF paragraph 73** (housing supply) 

The development should be assessed against these policies to ensure full compliance.

### Retrieved context (8 chunks — verify citations against these)

**[1] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.38 (city: leicester, score 0.8077)**
> paragraph 4.5 of the Plan and also help meet the economic, social and 
environmental objectives of the planning system as set out in paragraph 8 of 
the NPPF. 
Policy SL01.  Location of Development 
Development within the Leicester City administrative boundary will be located 
in accordance with the spatial strategy outlined below and as shown on 
Diagram 2 Growth in the Leicester Urban Area. 
Hou

**[2] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.38 (city: leicester, score 0.8077)**
> paragraph 4.5 of the Plan and also help meet the economic, social and 
environmental objectives of the planning system as set out in paragraph 8 of 
the NPPF. 
Policy SL01.  Location of Development 
Development within the Leicester City administrative boundary will be located 
in accordance with the spatial strategy outlined below and as shown on 
Diagram 2 Growth in the Leicester Urban Area. 
Hou

**[3] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.10 (city: leicester, score 0.7736)**
> 1.1 In 2021 the Government published a revised National Planning Policy 
Framework (NPPF). The NPPF requires local planning authorities like Leicester 
City Council to support sustainable development and to plan positively for it, by 
preparing new local plans. 
1.2 Leicester City Council has produced this Local Plan, which sets out the 
vision and objectives for the growth of the city over the ne

**[4] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.10 (city: leicester, score 0.7736)**
> 1.1 In 2021 the Government published a revised National Planning Policy 
Framework (NPPF). The NPPF requires local planning authorities like Leicester 
City Council to support sustainable development and to plan positively for it, by 
preparing new local plans. 
1.2 Leicester City Council has produced this Local Plan, which sets out the 
vision and objectives for the growth of the city over the ne

**[5] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.28 (city: leicester, score 0.7663)**
> appropriate proposals can be approved wherever possible to secure 
development that improves the economic, social and environmental 
conditions in Leicester 
c) Planning applications that accord with policies in the adopted development 
plan will be approved unless material considerations indicate otherwise 
d) Where there are no relevant development plan policies, or the policies 
28

**[6] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.28 (city: leicester, score 0.7663)**
> appropriate proposals can be approved wherever possible to secure 
development that improves the economic, social and environmental 
conditions in Leicester 
c) Planning applications that accord with policies in the adopted development 
plan will be approved unless material considerations indicate otherwise 
d) Where there are no relevant development plan policies, or the policies 
28

**[7] Nottingham_LAPP_2020.pdf p.194 (city: nottingham, score 0.6352)**
> Section 6: Development Management Policies – Making it Happen 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 186 
 
 
 
Justification 
 
Housing 
 
6.13  The NPPF requires local authorities to identify annually a supply of specific deliverable 

**[8] Nottingham_LAPP_2020.pdf p.194 (city: nottingham, score 0.6352)**
> Section 6: Development Management Policies – Making it Happen 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 186 
 
 
 
Justification 
 
Housing 
 
6.13  The NPPF requires local authorities to identify annually a supply of specific deliverable 

### Rubric (enter in the Evaluate page for `LEI-PC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEI-SA-01 — BASELINE

**City:** leicester | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Waterside, Leicester, for a residential-led mixed-use development. Identify the relevant policies from the Leicester Local Plan 2020-2036 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy SL01, Policy DQP01 — source: `Leicester_Local_Plan_2020-2036_Adopted_2026.pdf`

### Output (baseline)

### Assessment of a 2-Hectare Former Industrial Site in Waterside, Leicester for Residential-Led Mixed-Use Development

#### 1. **Site Context and Suitability**
The Waterside area of Leicester has been identified for regeneration and redevelopment, particularly given its proximity to the city centre and the River Soar. The former industrial site presents an opportunity for a residential-led mixed-use development, which aligns with broader urban renewal objectives.

#### 2. **Relevant Policies from the Leicester Local Plan 2020-2036**
The Leicester Local Plan outlines several key policies that would be relevant to assessing the suitability of the site for development:

- **Policy SS1: Sustainable Development** - This policy emphasizes the need for developments to contribute to sustainable growth, including the efficient use of land and resources. A residential-led mixed-use development could enhance local amenities and support sustainable transport options.

- **Policy H1: Housing Requirement** - The plan sets out the need for new housing to meet demand. A residential component on this site would contribute to the overall housing supply in Leicester, particularly in a location that is likely to attract residents due to its urban setting.

- **Policy H2: Housing Mix** - This policy encourages a mix of housing types and tenures to meet diverse community needs. A mixed-use development could incorporate affordable housing, which is a priority in Leicester.

- **Policy E1: Employment Land** - Given the site's former industrial use, this policy requires consideration of the potential for retaining employment uses. However, if the site is no longer viable for industrial use, a residential-led approach may be justified, particularly if it can demonstrate benefits to the local economy.

- **Policy D1: Design Quality** - This policy emphasizes high-quality design that enhances the character of the area. Any proposed development will need to demonstrate how it contributes positively to the local context.

- **Policy EN1: Biodiversity and Geodiversity** - Development proposals must consider the impact on local biodiversity. An ecological assessment may be required to ensure that any development does not adversely affect local habitats.

- **Policy EN3: Pollution** - This policy addresses issues of air quality, noise, and contamination. Given the site's industrial history, a thorough site investigation will be necessary to assess any contamination and ensure that the site is suitable for residential use.

#### 3. **Likely Constraints**
While the site presents opportunities, several constraints must be considered:

- **Contamination**: As a former industrial site, there may be soil and groundwater contamination that needs to be remediated before residential use can be established. A Phase 1 and potentially a Phase 2 site investigation will be necessary.

- **Transport and Accessibility**: The site’s accessibility to public transport and local amenities will be crucial. The development should promote sustainable transport options, in line with the NPPF’s emphasis on reducing reliance on private vehicles (NPPF, Paragraph 104).

- **Flood Risk**: Proximity to the River Soar may raise flood risk concerns. A Flood Risk Assessment (FRA) will be required to ensure that the development complies with Policy EN5: Flood Risk and Water Management.

- **Heritage Considerations**: If there are any listed buildings or conservation areas nearby, the development must consider the impact on the historic environment, as outlined in NPPF Section 16.

- **Community Infrastructure**: The development should contribute to local infrastructure needs, including schools, healthcare, and open spaces, in line with Policy IN1: Infrastructure Delivery.

#### 4. **Conclusion**
In summary, the 2-hectare former industrial site in Waterside, Leicester, has potential for a residential-led mixed-use development, aligning with local and national planning policies aimed at sustainable growth and urban regeneration. However, careful consideration of contamination, transport accessibility, flood risk, and community infrastructure will be essential to ensure compliance with the Leicester Local Plan and the NPPF. A comprehensive planning application that addresses these factors will be necessary to move forward with the development.

### Rubric (enter in the Evaluate page for `LEI-SA-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LEI-SA-01 — RAG

**City:** leicester | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Waterside, Leicester, for a residential-led mixed-use development. Identify the relevant policies from the Leicester Local Plan 2020-2036 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy SL01, Policy DQP01 — source: `Leicester_Local_Plan_2020-2036_Adopted_2026.pdf`

### Output (rag)

To assess the suitability of a hypothetical 2-hectare former industrial site in the Waterside area of Leicester for a residential-led mixed-use development, we can draw upon several relevant policies from the Leicester Local Plan 2020-2036, as well as consider potential constraints.

### Relevant Policies

1. **Waterside Vision and SPD**: The vision for Leicester’s Waterside aims to create a thriving urban neighbourhood that is vibrant and conducive to living. The council has adopted a 'Waterside' Supplementary Planning Document (SPD) that outlines a development vision for the area, emphasizing the importance of creating spaces for local businesses and reusing redundant buildings (Extract 1). This indicates a supportive framework for mixed-use developments that include residential components.

2. **Indicative Capacity for Dwellings**: The Local Plan identifies strategic sites in the Waterside area with an indicative capacity of at least 670 dwellings (Extract 3). This suggests that the area is designated for residential development, which aligns with the proposed use of the site.

3. **Support for Office Growth**: The Local Plan supports additional office growth within the Waterside Regeneration area, provided it complements existing residential-led regeneration (Extract 5). This indicates that a mixed-use development that includes residential and office space would be in line with local policy objectives.

4. **Economic, Social, and Environmental Objectives**: The development of the site would contribute to meeting the economic, social, and environmental objectives of the planning system as outlined in paragraph 8 of the NPPF (Extract 3). This is crucial for justifying the development in terms of broader planning goals.

### Likely Constraints

1. **Existing Use and Redevelopment**: As the site is a former industrial area, there may be constraints related to contamination or the need for remediation before residential use can be established. This is a common issue with former industrial sites and would need to be addressed through appropriate assessments and potential cleanup measures.

2. **Compatibility with Surrounding Uses**: While the Local Plan supports mixed-use developments, the compatibility of residential uses with any remaining industrial or commercial activities in the vicinity must be considered. Noise, traffic, and other impacts from adjacent uses could pose challenges.

3. **Infrastructure and Services**: The capacity of local infrastructure (e.g., roads, public transport, schools, and healthcare) to support additional residential units must be evaluated. The Local Plan indicates that developments should help address key planning issues, which may include ensuring adequate infrastructure is in place (Extract 3).

4. **Planning Obligations**: Any development may be subject to planning obligations under Policy WDC18, which could require contributions to local infrastructure or community facilities (Extract 7). This could impact the viability of the proposed development.

### Conclusion

In summary, the hypothetical 2-hectare former industrial site in the Waterside area is suitable for a residential-led mixed-use development, supported by the vision and policies outlined in the Leicester Local Plan 2020-2036. However, careful consideration of potential constraints, particularly regarding site remediation, compatibility with surrounding uses, and infrastructure capacity, will be essential to ensure a successful development that aligns with local planning objectives.

### Retrieved context (8 chunks — verify citations against these)

**[1] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.210 (city: leicester, score 0.7813)**
> Housing at Waterside 
2. Waterside 
9.40 The vision for Leicester’s Waterside is to create a thriving urban 
neighbourhood that provides a unique and vibrant place to live. The council 
has adopted a ‘Waterside’ SPD which provides a development vision for the 
area and provides further guidance around its delivery. Development will 
provide new offices and space for local businesses to flourish an

**[2] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.210 (city: leicester, score 0.7813)**
> Housing at Waterside 
2. Waterside 
9.40 The vision for Leicester’s Waterside is to create a thriving urban 
neighbourhood that provides a unique and vibrant place to live. The council 
has adopted a ‘Waterside’ SPD which provides a development vision for the 
area and provides further guidance around its delivery. Development will 
provide new offices and space for local businesses to flourish an

**[3] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.45 (city: leicester, score 0.7668)**
> and a secondary school. In total, this strategic site has an indicative capacity of 
at least 670 dwellings. The smaller parcel has been identified for employment 
use. This strategic site will help Leicester to meet the economic, social and 
environmental objectives of the planning system as set out in paragraph 8 
of the NPPF. It will also help to address the following key planning issues in 
Le

**[4] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.45 (city: leicester, score 0.7668)**
> and a secondary school. In total, this strategic site has an indicative capacity of 
at least 670 dwellings. The smaller parcel has been identified for employment 
use. This strategic site will help Leicester to meet the economic, social and 
environmental objectives of the planning system as set out in paragraph 8 
of the NPPF. It will also help to address the following key planning issues in 
Le

**[5] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.40 (city: leicester, score 0.762)**
> (i), C3) 
Additional office growth will be supported within the Waterside Regeneration 
area where it compliments the existing residential led regeneration. 
Former Western Park Golf Course 
4.25 The Local Plan identifies 52.85 ha of land in the western part of the city 
within the Leicester City administrative boundary. This land forms part of a 
larger area which lies within Blaby District Counc

**[6] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.40 (city: leicester, score 0.762)**
> (i), C3) 
Additional office growth will be supported within the Waterside Regeneration 
area where it compliments the existing residential led regeneration. 
Former Western Park Golf Course 
4.25 The Local Plan identifies 52.85 ha of land in the western part of the city 
within the Leicester City administrative boundary. This land forms part of a 
larger area which lies within Blaby District Counc

**[7] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.443 (city: leicester, score 0.7589)**
> • Policy WDC18: Planning Obligations
City of Leicester Local Plan (2006) – Saved Policies Version 
• PS05. Central Office Core (New Business Quarter) 
•PS06 St. George’s Residential and Working Community 
•PS07. Waterside 
• PS08. Science and Technology Based Business Park and Environs - Abbey 
Meadows 
• PS09. Potential Development Areas (PDAs) 
•PS09a. Proposed PDA Uses Within Strategic Regener

**[8] Leicester_Local_Plan_2020-2036_Adopted_2026.pdf p.443 (city: leicester, score 0.7589)**
> • Policy WDC18: Planning Obligations
City of Leicester Local Plan (2006) – Saved Policies Version 
• PS05. Central Office Core (New Business Quarter) 
•PS06 St. George’s Residential and Working Community 
•PS07. Waterside 
• PS08. Science and Technology Based Business Park and Environs - Abbey 
Meadows 
• PS09. Potential Development Areas (PDAs) 
•PS09a. Proposed PDA Uses Within Strategic Regener

### Rubric (enter in the Evaluate page for `LEI-SA-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LIV-SA-01 — BASELINE

**City:** liverpool | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Baltic Triangle, Liverpool, for a residential-led mixed-use development. Identify the relevant policies from the Liverpool Local Plan 2013-2033 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy H1, Policy H12, Policy H14, Policy UD1 — source: `Liverpool_Local_Plan_2013-2033.pdf`

### Output (baseline)

### Assessment of a 2-Hectare Former Industrial Site in the Baltic Triangle, Liverpool for Residential-Led Mixed-Use Development

#### Site Context
The Baltic Triangle is a vibrant area in Liverpool known for its creative industries, cultural venues, and emerging residential developments. The site in question, being a former industrial site, presents both opportunities and challenges for redevelopment.

#### Relevant Policies from the Liverpool Local Plan 2013-2033

1. **Policy SD1: Sustainable Development**
   - This policy emphasizes the need for sustainable development that meets the needs of the present without compromising future generations. A residential-led mixed-use development could align with this policy if it incorporates sustainable design principles, energy efficiency, and promotes social inclusion.

2. **Policy HC1: Housing Supply**
   - The Local Plan aims to deliver a significant number of new homes. The redevelopment of this site for residential use would contribute to the housing supply target, particularly in a city where there is a demand for diverse housing options.

3. **Policy HC2: Affordable Housing**
   - This policy requires a proportion of new housing developments to be affordable. The proposal should include affordable housing units to comply with this policy, which is crucial for addressing local housing needs.

4. **Policy CC1: Climate Change**
   - Developments must demonstrate how they will mitigate and adapt to climate change. The proposal should include measures such as sustainable drainage systems (SuDS), energy-efficient building designs, and the use of renewable energy sources.

5. **Policy EQ2: Design Quality**
   - This policy stresses the importance of high-quality design that enhances the character of the area. The development should reflect the unique identity of the Baltic Triangle, incorporating innovative design that complements the existing urban fabric.

6. **Policy EQ3: Pollution**
   - Given the site's industrial history, the proposal must address potential contamination issues and ensure that the development does not adversely affect air quality or noise levels. A thorough site investigation and remediation plan will be necessary.

7. **Policy TC1: Town Centre Uses**
   - The Local Plan encourages mixed-use developments that include retail, leisure, and community facilities. A residential-led scheme should integrate commercial spaces to support local businesses and enhance the vibrancy of the area.

#### Likely Constraints

1. **Contamination and Remediation**
   - As a former industrial site, there may be soil and groundwater contamination that needs to be assessed and remediated. A Phase 1 and potentially a Phase 2 Environmental Assessment will be required to identify and mitigate any risks.

2. **Infrastructure Capacity**
   - The local infrastructure, including transport, utilities, and public services, must be assessed to ensure it can accommodate the additional residential units. Any necessary upgrades or contributions to local infrastructure may be required.

3. **Heritage Considerations**
   - The Baltic Triangle has a rich industrial heritage, and any development must consider the impact on heritage assets. A heritage impact assessment may be necessary if the site is near listed buildings or conservation areas.

4. **Community Engagement**
   - Engaging with the local community and stakeholders is essential to ensure that the development meets local needs and aspirations. This aligns with the NPPF's emphasis on community involvement in the planning process (NPPF, Paragraph 39).

5. **Transport and Accessibility**
   - The site’s accessibility to public transport and pedestrian routes will be crucial. The development should promote sustainable transport options, in line with the NPPF’s objectives for sustainable transport (NPPF, Paragraph 104).

#### Conclusion
The 2-hectare former industrial site in the Baltic Triangle has significant potential for a residential-led mixed-use development, aligning with several policies in the Liverpool Local Plan 2013-2033. However, careful consideration of constraints such as contamination, infrastructure capacity, and community engagement will be essential to ensure a successful and sustainable development. A comprehensive planning application that addresses these factors will be necessary to navigate the planning process effectively.

### Rubric (enter in the Evaluate page for `LIV-SA-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LIV-SA-01 — RAG

**City:** liverpool | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Baltic Triangle, Liverpool, for a residential-led mixed-use development. Identify the relevant policies from the Liverpool Local Plan 2013-2033 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy H1, Policy H12, Policy H14, Policy UD1 — source: `Liverpool_Local_Plan_2013-2033.pdf`

### Output (rag)

To assess the suitability of a hypothetical 2-hectare former industrial site in the Baltic Triangle, Liverpool, for a residential-led mixed-use development, we must consider the relevant policies from the Liverpool Local Plan 2013-2033 and any potential constraints.

### Relevant Policies

1. **Employment Land Supply Assessment**:
   The Liverpool Local Plan indicates that an assessment of existing and potential employment sites has been conducted to identify employment land supply (Extract 1). This assessment suggests that some sites previously designated for industrial/business purposes may no longer be attractive for purely industrial uses. Therefore, if the former industrial site in the Baltic Triangle is identified as one of these less attractive sites, it may be more suitable for alternative uses, including residential-led mixed-use development.

2. **Use Class Order and Non-Industrial Proposals**:
   According to Extract 3, proposals for non-industrial purposes in Primarily Industrial/Business Areas must demonstrate that they meet specific criteria, especially where permitted development rights do not apply. This means that any residential-led mixed-use proposal would need to clearly justify the change of use from industrial to residential, potentially demonstrating a lack of demand for industrial use or the site's unsuitability for such purposes.

3. **Opportunities for Economic Development**:
   The Local Plan highlights significant opportunities for major economic development in areas with concentrations of vacant land and buildings, particularly in north Liverpool (Extract 5). The Baltic Triangle, being a part of this area, may benefit from such development opportunities, especially if it aligns with the broader vision for mixed-use developments in the city.

4. **Liverpool Waters Development**:
   While not directly related to the Baltic Triangle, the mention of "Liverpool Waters" as a major mixed-use development opportunity (Extract 6) indicates a city-wide strategy to promote mixed-use developments. This context supports the idea that residential-led mixed-use developments are encouraged in Liverpool, particularly in areas undergoing transformation.

### Likely Constraints

1. **Justification for Change of Use**:
   The primary constraint will be the need to justify the change of use from industrial to residential. The proposal must demonstrate that the site is no longer viable for industrial purposes, which may require market analysis and evidence of demand for residential use.

2. **Local Plan Policies**:
   The proposal must comply with the policies outlined in the Liverpool Local Plan, particularly those related to the use of Primarily Industrial/Business Areas. If the site is still designated as such, the proposal may face significant scrutiny and require a robust justification to gain approval.

3. **Infrastructure and Community Needs**:
   Any residential-led mixed-use development will also need to consider the existing infrastructure and community needs in the Baltic Triangle. This includes access to transport, amenities, and services, which are critical for residential developments.

### Conclusion

In summary, the hypothetical 2-hectare former industrial site in the Baltic Triangle could be suitable for a residential-led mixed-use development, provided that it can demonstrate a lack of viability for industrial use and comply with the relevant policies of the Liverpool Local Plan. The proposal will need to address the constraints related to the justification for change of use and ensure alignment with the broader development goals of the city.

### Retrieved context (8 chunks — verify citations against these)

**[1] Liverpool_Local_Plan_2013-2033.pdf p.109 (city: liverpool, score 0.7599)**
> 7.8 As part of the ELS process, an assessment of existing and potential employment sites has 
been undertaken to identify emplo
yment land supply with potential to meet the residual requirement. 
This includes a review of sites allocated or designated for industrial/business purposes, office 
development and mixed-use in the Liverpool Unitary Development Plan (2002). The assessment 
identifies tha

**[2] Liverpool_Local_Plan_2013-2033.pdf p.109 (city: liverpool, score 0.7599)**
> 7.8 As part of the ELS process, an assessment of existing and potential employment sites has 
been undertaken to identify emplo
yment land supply with potential to meet the residual requirement. 
This includes a review of sites allocated or designated for industrial/business purposes, office 
development and mixed-use in the Liverpool Unitary Development Plan (2002). The assessment 
identifies tha

**[3] Liverpool_Local_Plan_2013-2033.pdf p.111 (city: liverpool, score 0.7573)**
> 3. Where permitted development rights do not apply or the proposal involves changes which fall 
outside those allowed within the Use Class Order proposals f
or the use of Primarily Industrial/ 
Business Areas and Sites, for non-industrial purposes, should clearly demonstrate that: 
30 Liverpool City Region Assessment of the Supply of Large-Scale B8 Sites (June 2018, but published later).The Liverp

**[4] Liverpool_Local_Plan_2013-2033.pdf p.111 (city: liverpool, score 0.7573)**
> 3. Where permitted development rights do not apply or the proposal involves changes which fall 
outside those allowed within the Use Class Order proposals f
or the use of Primarily Industrial/ 
Business Areas and Sites, for non-industrial purposes, should clearly demonstrate that: 
30 Liverpool City Region Assessment of the Supply of Large-Scale B8 Sites (June 2018, but published later).The Liverp

**[5] Liverpool_Local_Plan_2013-2033.pdf p.35 (city: liverpool, score 0.7531)**
> 3.45 In addition, the concentrations of vacant land and buildings within north Liverpool present 
significant opportunities for major economic de
velopment. “Liverpool Waters” is the largest single 
development opportunity in the City, comprising some 60 hectares of land (stretching from Princes 
Dock, on the edge of the City Centre, north to Bramley Moore dock) and is owned by Peel Holdings. 
It 

**[6] Liverpool_Local_Plan_2013-2033.pdf p.35 (city: liverpool, score 0.7531)**
> 3.45 In addition, the concentrations of vacant land and buildings within north Liverpool present 
significant opportunities for major economic de
velopment. “Liverpool Waters” is the largest single 
development opportunity in the City, comprising some 60 hectares of land (stretching from Princes 
Dock, on the edge of the City Centre, north to Bramley Moore dock) and is owned by Peel Holdings. 
It 

**[7] Liverpool_Local_Plan_2013-2033.pdf p.15 (city: liverpool, score 0.7382)**
> Local Plan timescales, with some either adopted or at an advanced stage, it has not been possible 
for local authorities to act in tandem to identify sites to meet this need in the short term. However, the 
Liverpool Employment Land Study 2017, produced to support the Local Plan, in addition to meeting 
the City’s own employment land needs, identified 27.4 ha of land to meet the sub-regional deman

**[8] Liverpool_Local_Plan_2013-2033.pdf p.15 (city: liverpool, score 0.7382)**
> Local Plan timescales, with some either adopted or at an advanced stage, it has not been possible 
for local authorities to act in tandem to identify sites to meet this need in the short term. However, the 
Liverpool Employment Land Study 2017, produced to support the Local Plan, in addition to meeting 
the City’s own employment land needs, identified 27.4 ha of land to meet the sub-regional deman

### Rubric (enter in the Evaluate page for `LIV-SA-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LIV-PC-01 — BASELINE

**City:** liverpool | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Liverpool city centre comply with the housing policies of the Liverpool Local Plan 2013-2033 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy H1, Policy H12, Policy H14, NPPF para 11, NPPF para 120 — source: `Liverpool_Local_Plan_2013-2033.pdf`

### Output (baseline)

To assess whether the proposed 80-unit residential development on a brownfield site in Liverpool city centre complies with the housing policies of the Liverpool Local Plan 2013-2033 and the National Planning Policy Framework (NPPF) December 2024, we need to consider several key aspects of both documents.

### 1. **Liverpool Local Plan 2013-2033**

The Liverpool Local Plan outlines the strategic vision and policies for housing development within the city. Key policies relevant to the proposed development include:

- **Policy HC1: Housing Supply**: This policy emphasizes the need to deliver a sufficient supply of homes to meet the city's housing needs. The plan sets out a target for new housing units, and developments on brownfield sites are encouraged to contribute to this target. Given that the proposed development is on a brownfield site, it aligns with the objectives of this policy.

- **Policy HC2: Affordable Housing**: This policy requires a proportion of new housing developments to be affordable. The specific percentage may vary depending on the location and type of development. The proposal should include an assessment of how many of the 80 units will be affordable, as this will be a critical factor in compliance.

- **Policy HC3: Housing Mix**: This policy encourages a mix of housing types and sizes to meet the diverse needs of the community. The proposed development should demonstrate how it addresses this requirement, potentially through a mix of one, two, and three-bedroom units.

- **Policy CC1: Climate Change and Sustainable Development**: This policy requires developments to demonstrate how they will contribute to sustainable development, including energy efficiency and reducing carbon emissions. The proposal should include measures to meet these sustainability criteria.

### 2. **National Planning Policy Framework (NPPF) December 2024**

The NPPF provides a framework for planning decisions across England, with several key paragraphs relevant to housing development:

- **Paragraph 60**: This paragraph states that the government’s objective is to significantly boost the supply of homes. The proposed development of 80 units contributes positively to this objective, particularly in a city centre location where there is a demand for housing.

- **Paragraph 68**: This paragraph encourages the development of small and medium-sized sites, which can help to meet housing needs. An 80-unit development can be considered a medium-sized site, thus supporting this policy direction.

- **Paragraph 74**: This paragraph emphasizes the importance of using brownfield land for development. The proposed site being brownfield aligns with national priorities for land use and sustainable development.

- **Paragraph 77**: This paragraph encourages local authorities to identify and bring forward land for housing, particularly in urban areas. The development in Liverpool city centre supports this aim by utilizing previously developed land.

### Conclusion

In summary, the proposed 80-unit residential development on a brownfield site in Liverpool city centre appears to comply with both the Liverpool Local Plan and the NPPF. Key policies from the Local Plan, such as HC1, HC2, HC3, and CC1, support the development of housing on brownfield sites, the provision of affordable housing, and the need for a mix of housing types. Additionally, the NPPF's emphasis on boosting housing supply, utilizing brownfield land, and supporting medium-sized developments further reinforces the proposal's compliance.

However, it is essential for the developer to provide detailed plans that address affordable housing provision, housing mix, and sustainability measures to ensure full compliance with the relevant policies. Engaging with the local planning authority early in the process can also help to identify any specific local requirements or considerations that may apply.

### Rubric (enter in the Evaluate page for `LIV-PC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LIV-PC-01 — RAG

**City:** liverpool | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Liverpool city centre comply with the housing policies of the Liverpool Local Plan 2013-2033 and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy H1, Policy H12, Policy H14, NPPF para 11, NPPF para 120 — source: `Liverpool_Local_Plan_2013-2033.pdf`

### Output (rag)

To assess whether a proposed 80-unit residential development on a brownfield site in Liverpool city centre complies with the housing policies of the Liverpool Local Plan 2013-2033 and the National Planning Policy Framework (NPPF) December 2024, we can draw on the relevant extracts from the provided context.

1. **Housing Requirement and Provision**: The Liverpool Local Plan indicates that the scale and location of housing growth necessary to meet the expanding population will need to be met within the built-up area, as Liverpool is predominantly urbanised (Extract 5, Page 133). This suggests that a brownfield site in the city centre is an appropriate location for residential development, aligning with the strategic requirement for housing.

2. **Site Allocations**: The Local Plan includes specific policies for residential development site allocations (Extract 7, Page 22). While the specific allocations are not detailed in the provided extracts, the mention of Policy H2 indicates that there are designated sites for residential development, which would likely include brownfield sites in the city centre.

3. **Monitoring Housing Supply**: The Local Plan states that Liverpool exceeded its housing requirement between 2016 and 2019, which allows for a 5% buffer in housing supply (Extract 3, Page 134). This indicates a proactive approach to housing delivery, suggesting that the council is supportive of new residential developments that contribute to meeting housing needs.

4. **Compliance with NPPF**: The Local Plan policies are stated to be in accordance with the NPPF (Extract 6, Page 133). The NPPF emphasizes the importance of using brownfield land for housing development (NPPF paragraph 117), which supports the proposed development on a brownfield site.

In summary, the proposed 80-unit residential development on a brownfield site in Liverpool city centre appears to comply with the housing policies of the Liverpool Local Plan 2013-2033 and the NPPF. The relevant policies include:

- **Liverpool Local Plan**: 
  - Policy H1 (Housing Requirement)
  - Policy H2 (Residential Development Site Allocations)
  
- **NPPF**: 
  - Paragraph 117 (encouraging the use of brownfield land for housing)

Given these considerations, the proposed development aligns with the strategic objectives of the Local Plan and the overarching principles of the NPPF regarding sustainable housing development.

### Retrieved context (8 chunks — verify citations against these)

**[1] Liverpool_Local_Plan_2013-2033.pdf p.3 (city: liverpool, score 0.7748)**
> Local Plan including all the development sites 
identified for future housing growth.
The comprehensive nature of the Local Plan 
proposals also includes specific provision to
protect the physical and built environment 
in terms of heritage assets and open 
space. These policies and proposals clearly 
demonstrate both the strength and depth of 
Liverpool’s commitment to protecting and
enhancing Li

**[2] Liverpool_Local_Plan_2013-2033.pdf p.3 (city: liverpool, score 0.7748)**
> Local Plan including all the development sites 
identified for future housing growth.
The comprehensive nature of the Local Plan 
proposals also includes specific provision to
protect the physical and built environment 
in terms of heritage assets and open 
space. These policies and proposals clearly 
demonstrate both the strength and depth of 
Liverpool’s commitment to protecting and
enhancing Li

**[3] Liverpool_Local_Plan_2013-2033.pdf p.134 (city: liverpool, score 0.7693)**
> 2019 found Liverpool had exceeded the housing requirement between 2016 and 2019 (by 181%) and 
therefore in accordance with NPPF a 5% buffer for Liverpool is appropriate. 
8.7 As part of the Local Plan monitoring framework, the number of housing permissions and 
completions are monitored and reported in the council's Authority Monitor
ing Report and the housing 
trajectory will be reviewed and upd

**[4] Liverpool_Local_Plan_2013-2033.pdf p.134 (city: liverpool, score 0.7693)**
> 2019 found Liverpool had exceeded the housing requirement between 2016 and 2019 (by 181%) and 
therefore in accordance with NPPF a 5% buffer for Liverpool is appropriate. 
8.7 As part of the Local Plan monitoring framework, the number of housing permissions and 
completions are monitored and reported in the council's Authority Monitor
ing Report and the housing 
trajectory will be reviewed and upd

**[5] Liverpool_Local_Plan_2013-2033.pdf p.133 (city: liverpool, score 0.7672)**
> 8 
8 Housing Provision 
Introduction 
8.1 As Liverpool is predominantly urbanised, the scale and location of housing growth necessary 
to meet the expanding population will need to be met within the built-up area. This Chapter sets out 
the str
ategic requirement, site allocations and development management policies for residential 
development. 
8.2 All the policies, in accordance with the Nation

**[6] Liverpool_Local_Plan_2013-2033.pdf p.133 (city: liverpool, score 0.7672)**
> 8 
8 Housing Provision 
Introduction 
8.1 As Liverpool is predominantly urbanised, the scale and location of housing growth necessary 
to meet the expanding population will need to be met within the built-up area. This Chapter sets out 
the str
ategic requirement, site allocations and development management policies for residential 
development. 
8.2 All the policies, in accordance with the Nation

**[7] Liverpool_Local_Plan_2013-2033.pdf p.22 (city: liverpool, score 0.7645)**
> 13. Policy CC18 St George’s Quarter 
14. Policy CC25 City Centre Student Accommodation 
15. P
olicy EC1 Employment Land Supply 
16. Policy EC2 Employment Areas (Paragraph 1) 
17. Policy EC5 Office Development 
18. Policy EC6 Mixed Use Areas and Sites for Various Types of Development 
19. Policy EC7 Liverpool John Lennon Airport 
20. Policy EC8 The Ports of Liverpool and Garston 
21. Policy H1 Hous

**[8] Liverpool_Local_Plan_2013-2033.pdf p.22 (city: liverpool, score 0.7645)**
> 13. Policy CC18 St George’s Quarter 
14. Policy CC25 City Centre Student Accommodation 
15. P
olicy EC1 Employment Land Supply 
16. Policy EC2 Employment Areas (Paragraph 1) 
17. Policy EC5 Office Development 
18. Policy EC6 Mixed Use Areas and Sites for Various Types of Development 
19. Policy EC7 Liverpool John Lennon Airport 
20. Policy EC8 The Ports of Liverpool and Garston 
21. Policy H1 Hous

### Rubric (enter in the Evaluate page for `LIV-PC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LON-ES-01 — BASELINE

**City:** london | **Category:** evidence_synthesis | **Difficulty:** medium

**Task:** Summarise the overall spatial strategy and housing requirement set out in the London Plan 2021, citing the key strategic policies (Policy H1, Policy H4, Policy H10 where relevant).

**Expected policies (check these in the source PDF):** Policy H1, Policy H4, Policy H10 — source: `London_Plan_2021.pdf`

### Output (baseline)

The London Plan 2021, which serves as the spatial development strategy for Greater London, outlines a comprehensive framework for managing growth and development in the capital. The overall spatial strategy is focused on sustainable development, promoting a compact city, and ensuring that growth is concentrated in locations with good public transport accessibility. This approach aims to enhance the quality of life for Londoners while addressing the pressing need for housing.

### Overall Spatial Strategy

The London Plan emphasizes the need for a balanced approach to development, integrating housing, economic growth, and environmental sustainability. Key elements of the spatial strategy include:

1. **Concentration of Growth**: The Plan directs growth towards Opportunity Areas, town centres, and areas with good public transport links, thereby promoting higher density development in these locations.
2. **Sustainable Development**: The strategy prioritizes sustainable development principles, including the efficient use of land, reducing carbon emissions, and enhancing green infrastructure.
3. **Mixed-Use Development**: Encouraging mixed-use developments is a core aspect of the strategy, which supports vibrant communities and reduces the need for travel.

### Housing Requirement

The London Plan sets a significant housing target to address the acute housing crisis in the capital. The key policies related to housing are as follows:

- **Policy H1: Increasing Housing Supply**: This policy establishes a strategic target of delivering at least 66,000 new homes per year across London. This figure is based on the latest evidence of housing need and aims to ensure that the demand for housing is met, particularly in light of population growth and economic development.

- **Policy H4: Delivering Affordable Housing**: This policy outlines the requirement for affordable housing within new developments. It sets a strategic target of 50% of all new homes to be affordable, with a focus on delivering a mix of tenures, including social rent, affordable rent, and intermediate housing. The policy emphasizes the importance of providing affordable housing to meet the diverse needs of London’s population.

- **Policy H10: Housing Size Mix**: This policy addresses the need for a diverse range of housing types and sizes to meet the varying needs of Londoners. It encourages developments to provide a mix of unit sizes, including family-sized homes, to ensure that the housing stock is inclusive and caters to different demographics, including families, single-person households, and older residents.

### Conclusion

In summary, the London Plan 2021 articulates a clear spatial strategy aimed at sustainable growth and development, with a strong emphasis on increasing housing supply to meet the needs of a growing population. The strategic policies (H1, H4, and H10) collectively underscore the importance of delivering a significant number of new homes, prioritizing affordable housing, and ensuring a diverse housing mix to create inclusive and vibrant communities across London. This framework is essential for guiding local planning authorities in their decision-making processes and ensuring that development aligns with the broader objectives of the London Plan.

### Rubric (enter in the Evaluate page for `LON-ES-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LON-ES-01 — RAG

**City:** london | **Category:** evidence_synthesis | **Difficulty:** medium

**Task:** Summarise the overall spatial strategy and housing requirement set out in the London Plan 2021, citing the key strategic policies (Policy H1, Policy H4, Policy H10 where relevant).

**Expected policies (check these in the source PDF):** Policy H1, Policy H4, Policy H10 — source: `London_Plan_2021.pdf`

### Output (rag)

The London Plan 2021 outlines a comprehensive spatial strategy aimed at addressing the housing needs of Londoners while ensuring sustainable development across the city. The key elements of this strategy are encapsulated in several policies, particularly Policy H1, Policy H4, and Policy H10.

### Overall Spatial Strategy

1. **Single Housing Market**: The London Plan treats London as a single housing market, which allows for a coordinated approach to planning and development across the boroughs. This strategic perspective enables the identification of sustainable locations for development and the effective allocation of resources (Extract 1, Extract 7).

2. **Ten-Year Housing Targets**: The Plan establishes ten-year housing targets for each borough, which are informed by a Strategic Housing Land Availability Assessment. This assessment identifies where the necessary homes can be delivered, ensuring that the housing needs of all Londoners are met (Extract 1).

3. **Focus on Sustainable Development**: The spatial strategy emphasizes the importance of focusing development in sustainable locations. This approach not only addresses housing needs but also integrates other land use requirements, promoting a holistic view of urban planning (Extract 7).

### Housing Requirement

1. **Policy H1 - Increasing Housing Supply**: This policy sets out the need to significantly increase the supply of homes across London. It emphasizes the importance of delivering a minimum of 10,000 additional homes per year, with a focus on affordable housing to meet the diverse needs of the population (not explicitly cited in the provided extracts but is a key component of the London Plan).

2. **Policy H4 - Delivering Affordable Housing**: This policy outlines the requirement for a minimum of 50% of new homes to be affordable in major development schemes. The aim is to address the acute shortage of affordable housing, which is critical for the recruitment and retention of essential public service workers (Extract 3).

3. **Policy H10 - Housing Size Mix**: This policy provides guidance on the mix of housing sizes that should be delivered in new developments. It aims to ensure that a range of housing types is available to meet the needs of different households, thereby promoting inclusivity and diversity within communities (not explicitly cited in the provided extracts but is a key component of the London Plan).

### Conclusion

In summary, the London Plan 2021 presents a strategic framework for addressing the housing crisis in London through a coordinated approach that prioritizes sustainable development and the delivery of affordable housing. The policies outlined, particularly Policy H1, H4, and H10, are integral to achieving these objectives and ensuring that the housing needs of all Londoners are met effectively. The emphasis on treating London as a single housing market allows for a more comprehensive and strategic approach to urban planning, which is essential for the city's resilience and growth.

### Retrieved context (8 chunks — verify citations against these)

**[1] London_Plan_2021.pdf p.35 (city: london, score 0.7874)**
> 1.4.4 The London Plan is able to look across the city to plan for the housing needs of 
all Londoners, treating London as a single housing market in a way that is not 
possible at a local level. In partnership with boroughs, the Mayor has undertaken 
a Strategic Housing Land Availability Assessment to identify where the homes 
London needs can be delivered. T en-year housing targets have been esta

**[2] London_Plan_2021.pdf p.35 (city: london, score 0.7874)**
> 1.4.4 The London Plan is able to look across the city to plan for the housing needs of 
all Londoners, treating London as a single housing market in a way that is not 
possible at a local level. In partnership with boroughs, the Mayor has undertaken 
a Strategic Housing Land Availability Assessment to identify where the homes 
London needs can be delivered. T en-year housing targets have been esta

**[3] London_Plan_2021.pdf p.40 (city: london, score 0.7814)**
> and planning authorities to determine what is needed where in order to plan 
for London’s future, using the framework established by the Mayor’s Strategic 
Infrastructure Investment Plan.
1.6.6 Ensuring sufficient housing at the right price is also key to the city’s resilience. 
The shortage of affordable housing in the capital is hindering the recruitment 
and retention of public service workers,

**[4] London_Plan_2021.pdf p.40 (city: london, score 0.7814)**
> and planning authorities to determine what is needed where in order to plan 
for London’s future, using the framework established by the Mayor’s Strategic 
Infrastructure Investment Plan.
1.6.6 Ensuring sufficient housing at the right price is also key to the city’s resilience. 
The shortage of affordable housing in the capital is hindering the recruitment 
and retention of public service workers,

**[5] London_Plan_2021.pdf p.198 (city: london, score 0.778)**
> programmes
62 Further details on LLR can be found in the London Housing Strategy
63 Mayor of London, 2018, London Housing Strategy: https://www.london.gov.uk/sites/default/
files/2018_lhs_london_housing_strategy.pdf
183
The London Plan 2021 – Chapter 4 Housing


**[6] London_Plan_2021.pdf p.198 (city: london, score 0.778)**
> programmes
62 Further details on LLR can be found in the London Housing Strategy
63 Mayor of London, 2018, London Housing Strategy: https://www.london.gov.uk/sites/default/
files/2018_lhs_london_housing_strategy.pdf
183
The London Plan 2021 – Chapter 4 Housing


**[7] London_Plan_2021.pdf p.173 (city: london, score 0.7763)**
> persons’ accommodation within the overall figure.
4.1.2 For the purposes of the Plan, London is considered as a single housing market 
area, with a series of complex and interlinked sub-markets. The advantage of 
strategic planning is that it allows London to focus development in the most 
sustainable locations, allowing all of London’s land use needs to be planned for 
with an understanding of ho

**[8] London_Plan_2021.pdf p.173 (city: london, score 0.7763)**
> persons’ accommodation within the overall figure.
4.1.2 For the purposes of the Plan, London is considered as a single housing market 
area, with a series of complex and interlinked sub-markets. The advantage of 
strategic planning is that it allows London to focus development in the most 
sustainable locations, allowing all of London’s land use needs to be planned for 
with an understanding of ho

### Rubric (enter in the Evaluate page for `LON-ES-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LON-SA-01 — BASELINE

**City:** london | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Isle of Dogs, London, for a residential-led mixed-use development. Identify the relevant policies from the London Plan 2021 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy H1, Policy H4, Policy H10, Policy D4 — source: `London_Plan_2021.pdf`

### Output (baseline)

### Assessment of a 2-Hectare Former Industrial Site in the Isle of Dogs for Residential-Led Mixed-Use Development

#### Introduction
The Isle of Dogs, located in the London Borough of Tower Hamlets, is an area undergoing significant transformation, with a shift from industrial uses to residential and mixed-use developments. This assessment evaluates the suitability of a hypothetical 2-hectare former industrial site for a residential-led mixed-use development, considering relevant policies from the London Plan 2021 and potential constraints.

#### Relevant Policies

1. **London Plan 2021**:
   - **Policy H1: Increasing Housing Supply**: This policy emphasizes the need to significantly increase housing supply across London. The site’s redevelopment for residential use aligns with this objective, particularly given the high demand for housing in the Isle of Dogs.
   - **Policy H2: Delivering Affordable Housing**: The London Plan sets a strategic target of 50% affordable housing on all new developments. A residential-led mixed-use scheme should incorporate a significant proportion of affordable units to meet local needs.
   - **Policy SD1: Opportunity Areas**: The Isle of Dogs is designated as an Opportunity Area, which encourages the development of residential and mixed-use schemes to optimize land use and support economic growth. This designation supports the suitability of the site for such development.
   - **Policy D1: London’s Form, Character and Capacity for Growth**: This policy encourages developments that enhance the character of the area while accommodating growth. The design of the proposed development should reflect the local context and contribute positively to the urban environment.
   - **Policy D3: Optimising Site Capacity through the Design-Led Approach**: This policy advocates for a design-led approach to maximize the potential of the site while ensuring that developments are of high quality and sustainable.

2. **Local Planning Policies**:
   - **Tower Hamlets Local Plan 2031**: The local plan supports the regeneration of the Isle of Dogs and encourages mixed-use developments that provide residential, commercial, and community facilities. Specific policies may include requirements for public realm improvements and contributions to local infrastructure.
   - **Policy S.1: Delivering Sustainable Development**: This policy emphasizes the need for developments to be sustainable, considering environmental impacts, social inclusion, and economic viability.

#### Likely Constraints

1. **Site Contamination**: As a former industrial site, there may be contamination issues that need to be addressed through appropriate remediation measures. A Phase 1 and potentially a Phase 2 Environmental Assessment will be necessary to assess the extent of contamination and the required mitigation strategies.

2. **Transport and Accessibility**: The site’s accessibility to public transport is crucial. The Isle of Dogs is served by the Docklands Light Railway (DLR) and is in proximity to the Canary Wharf area. However, any development must ensure that it does not exacerbate traffic congestion and provides adequate pedestrian and cycling infrastructure.

3. **Flood Risk**: The Isle of Dogs is located in a flood risk area due to its proximity to the River Thames. A Flood Risk Assessment (FRA) will be required to demonstrate that the development can be safely accommodated and that appropriate flood mitigation measures are in place.

4. **Heritage Considerations**: Depending on the site's history and any nearby listed buildings or conservation areas, there may be heritage constraints that need to be considered in the design and layout of the development.

5. **Community Infrastructure**: The development will need to contribute to local infrastructure, including schools, healthcare, and public spaces, to support the increased population. This may involve Section 106 agreements or Community Infrastructure Levy (CIL) contributions.

6. **Local Opposition and Community Engagement**: Given the history of development in the Isle of Dogs, there may be local opposition to new residential developments. Engaging with the community early in the planning process will be essential to address concerns and gain support.

#### Conclusion

The hypothetical 2-hectare former industrial site in the Isle of Dogs presents a suitable opportunity for a residential-led mixed-use development, aligning with the strategic objectives of the London Plan and local planning policies. However, careful consideration of potential constraints, including site contamination, flood risk, transport accessibility, and community infrastructure needs, will be essential to ensure a successful and sustainable development. Engaging with stakeholders and the local community will also be critical in navigating the planning process effectively.

### Rubric (enter in the Evaluate page for `LON-SA-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## LON-SA-01 — RAG

**City:** london | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in the Isle of Dogs, London, for a residential-led mixed-use development. Identify the relevant policies from the London Plan 2021 and any likely constraints.

**Expected policies (check these in the source PDF):** Policy H1, Policy H4, Policy H10, Policy D4 — source: `London_Plan_2021.pdf`

### Output (rag)

To assess the suitability of a hypothetical 2-hectare former industrial site in the Isle of Dogs, London, for a residential-led mixed-use development, we must consider several relevant policies from the London Plan 2021, as well as potential constraints.

### Relevant Policies

1. **Policy E4 - Land for Industry, Logistics and Services**: This policy emphasizes the importance of industrial land in supporting London’s economy. It states that mixed-use or residential development proposals on Non-Designated Industrial Sites should only be supported if there is no reasonable prospect of the site being used for industrial purposes (Extract 1 and 2). Therefore, a key consideration will be whether there is evidence that the site has no reasonable prospect for industrial use.

2. **Policy E5 - Strategic Industrial Locations (SIL)**: While the site in question is a former industrial site, it is important to assess its proximity to SILs and whether it complements the provision of sustainable distribution services in the area (Extract 3 and 4). If the site is near a SIL, this could pose a constraint on its redevelopment for residential purposes.

3. **Affordable Housing Requirement**: According to the London Plan, if the residential proposal results in a net loss of industrial capacity, it is expected to deliver at least 50% affordable housing (Extract 5 and 6). This requirement will significantly impact the viability of the proposed development.

4. **Co-location of Uses**: The London Plan allows for the co-location of industrial uses with residential and other uses as part of a plan-led or masterplanning process (Extract 1 and 2). This could be a potential avenue for development if the site can accommodate both uses effectively.

### Likely Constraints

1. **Industrial Use Viability**: The primary constraint will be demonstrating that there is no reasonable prospect of the site being used for industrial purposes. This may require market assessments or evidence of lack of demand for industrial space in the area.

2. **Proximity to SILs**: If the site is located near a Strategic Industrial Location, there may be additional scrutiny regarding the loss of industrial capacity and the potential impact on the local economy.

3. **Affordable Housing Delivery**: The requirement to provide at least 50% affordable housing could affect the financial viability of the project, especially if the site is expected to deliver significant residential units.

4. **Local Planning Context**: Any local planning policies or supplementary planning documents that may apply to the Isle of Dogs should also be reviewed, as they could impose additional requirements or constraints on the development.

### Conclusion

In summary, while there is potential for a residential-led mixed-use development on the former industrial site in the Isle of Dogs, it is crucial to address the requirements of the London Plan, particularly regarding the viability of industrial use and the affordable housing mandate. A thorough assessment of the local market and planning context will be essential to determine the feasibility of the proposed development.

### Retrieved context (8 chunks — verify citations against these)

**[1] London_Plan_2021.pdf p.273 (city: london, score 0.6851)**
> scope for co-locating industrial uses with residential and other uses may be 
considered. This should also be part of a plan-led or masterplanning process.
C Mixed-use or residential development proposals on Non-Designated 
Industrial Sites should only be supported where:
1) there is no reasonable prospect of the site being used for the industrial 
and related purposes set out in Part A of Policy 

**[2] London_Plan_2021.pdf p.273 (city: london, score 0.6851)**
> scope for co-locating industrial uses with residential and other uses may be 
considered. This should also be part of a plan-led or masterplanning process.
C Mixed-use or residential development proposals on Non-Designated 
Industrial Sites should only be supported where:
1) there is no reasonable prospect of the site being used for the industrial 
and related purposes set out in Part A of Policy 

**[3] London_Plan_2021.pdf p.272 (city: london, score 0.6796)**
> assessments and should complement provision in SILs. Inner London sites 
providing sustainable distribution services for the Central Activities Zone and 
Northern Isle of Dogs may be particularly appropriate for this designation.
257
The London Plan 2021 – Chapter 6 Economy


**[4] London_Plan_2021.pdf p.272 (city: london, score 0.6795)**
> assessments and should complement provision in SILs. Inner London sites 
providing sustainable distribution services for the Central Activities Zone and 
Northern Isle of Dogs may be particularly appropriate for this designation.
257
The London Plan 2021 – Chapter 6 Economy


**[5] London_Plan_2021.pdf p.189 (city: london, score 0.6717)**
> 4.4.8 Most industrial land fulfils a vital role in supporting London’s economy. 
However, it is occasionally deemed appropriate for residential uses. In these 
circumstances, there is potential for a significant difference in value between the 
two uses. The Mayor expects that residential proposals on industrial land should 
deliver at least 50 per cent affordable housing where the scheme would re

**[6] London_Plan_2021.pdf p.189 (city: london, score 0.6717)**
> 4.4.8 Most industrial land fulfils a vital role in supporting London’s economy. 
However, it is occasionally deemed appropriate for residential uses. In these 
circumstances, there is potential for a significant difference in value between the 
two uses. The Mayor expects that residential proposals on industrial land should 
deliver at least 50 per cent affordable housing where the scheme would re

**[7] London_Plan_2021.pdf p.378 (city: london, score 0.6696)**
> assessing demand for industrial land (see Policy E4 Land for industry, logistics 
and services to support London’s economic function, Policy E5 Strategic 
Industrial Locations (SIL), Policy E6 Locally Significant Industrial Sites and Policy 
E7 Industrial intensification, co-location and substitution).
9.6.8 The Mayor will work with network operators, developers, councils and 
Government to develo

**[8] London_Plan_2021.pdf p.378 (city: london, score 0.6696)**
> assessing demand for industrial land (see Policy E4 Land for industry, logistics 
and services to support London’s economic function, Policy E5 Strategic 
Industrial Locations (SIL), Policy E6 Locally Significant Industrial Sites and Policy 
E7 Industrial intensification, co-location and substitution).
9.6.8 The Mayor will work with network operators, developers, councils and 
Government to develo

### Rubric (enter in the Evaluate page for `LON-SA-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NEW-ST-01 — BASELINE

**City:** newcastle | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030 was adopted in 2015, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (baseline)

As an experienced UK planning consultant, I can provide a detailed analysis of how the December 2024 revisions to the National Planning Policy Framework (NPPF) may interact with the Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030, which was adopted in 2015. The key areas of potential tension or supersession include the grey belt designation, mandatory housing targets, and amendments to affordable housing policies.

### 1. Grey Belt Designation

**NPPF Changes**: The December 2024 revision introduces a new designation known as the "grey belt," which aims to provide a more flexible approach to land use, particularly in areas that are not designated as green belt but still require protection from inappropriate development.

**Tension with Adopted Plan**: The Core Strategy and Urban Core Plan may have specific designations and policies regarding green belt and other protected areas. If the adopted plan does not recognize the grey belt or fails to align with the new NPPF guidance, there could be conflicts regarding development proposals in these areas. The local plan may need to be reviewed and potentially amended to incorporate the grey belt designation and its implications for development control.

### 2. Mandatory Housing Targets

**NPPF Changes**: The December 2024 NPPF introduces mandatory housing targets that local authorities must meet, which are based on a national assessment of housing need. This represents a shift from the previous framework, which allowed for more local discretion in setting housing targets.

**Tension with Adopted Plan**: The Core Strategy and Urban Core Plan may have established housing targets that are lower than those mandated by the new NPPF. This could create a significant challenge for Gateshead and Newcastle, as they may be required to increase their housing delivery significantly to comply with the new targets. The local authorities will need to assess their housing land supply and potentially revise their housing policies to ensure compliance with the NPPF, which could lead to increased pressure on land use and infrastructure.

### 3. Affordable Housing Amendments

**NPPF Changes**: The December 2024 revision includes amendments to the policies surrounding affordable housing, emphasizing the need for a greater proportion of affordable homes in new developments and potentially altering the thresholds for when affordable housing contributions are required.

**Tension with Adopted Plan**: The Core Strategy and Urban Core Plan may have specific thresholds and percentages for affordable housing that do not align with the new requirements. If the adopted plan sets lower expectations for affordable housing provision, this could lead to conflicts in planning applications and a potential shortfall in affordable housing delivery. Local authorities will need to review their policies to ensure they meet the new standards, which may require a comprehensive review of the plan and associated viability assessments.

### Conclusion

In summary, the December 2024 revisions to the NPPF introduce significant changes that could supersede or create tension with the existing Core Strategy and Urban Core Plan for Gateshead and Newcastle. The local authorities will need to undertake a thorough review of their planning policies to ensure compliance with the new national framework, particularly concerning the grey belt designation, mandatory housing targets, and affordable housing provisions. This may involve a formal review process, public consultation, and potential amendments to the local plan to align with the updated national policies. 

It is advisable for the local planning authorities to engage with stakeholders and consider the implications of these changes on their strategic objectives, community needs, and overall sustainability goals.

### Rubric (enter in the Evaluate page for `NEW-ST-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NEW-ST-01 — RAG

**City:** newcastle | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030 was adopted in 2015, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (rag)

The provided context from the "Core Strategy and Urban Core Plan for Gateshead and Newcastle upon Tyne 2010-2030" (adopted March 2015) does not contain specific references to the December 2024 changes to the National Planning Policy Framework (NPPF), such as the introduction of grey belt designations, mandatory housing targets, or amendments to affordable housing policies. Therefore, I will supplement the information from my knowledge of UK planning policy to address your query.

1. **Grey Belt Designations**: The introduction of grey belt designations in the December 2024 NPPF revision may create tension with existing policies in the Core Strategy, particularly those that prioritize urban development in the Urban Core (Policy CS2). The Core Strategy emphasizes the Urban Core as a strategic priority for development to enhance economic prosperity, which may conflict with restrictions imposed by grey belt designations that limit development in certain areas.

2. **Mandatory Housing Targets**: The December 2024 NPPF revision introduces mandatory housing targets that local authorities must meet. The Core Strategy outlines a framework for meeting development needs but does not specify numerical housing targets. If the Core Strategy's housing delivery approach does not align with the new mandatory targets, this could create a conflict, necessitating a review or amendment of the Core Strategy to ensure compliance with national policy.

3. **Affordable Housing Amendments**: Changes to affordable housing requirements in the December 2024 NPPF may also supersede or create tension with the existing policies in the Core Strategy. If the new NPPF mandates higher percentages of affordable housing or different definitions of what constitutes affordable housing, the Core Strategy's existing provisions may need to be revised to align with these new requirements.

In summary, while the Core Strategy and Urban Core Plan provides a framework for development in Gateshead and Newcastle, the December 2024 changes to the NPPF regarding grey belt designations, mandatory housing targets, and affordable housing could create conflicts or necessitate amendments to ensure compliance with national policy. The specific policies in the Core Strategy that may be affected include Policy CS2 (Urban Core development priority) and any related housing policies that may not align with the new national standards.

### Retrieved context (8 chunks — verify citations against these)

**[1] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.1 (city: newcastle, score 0.8764)**
> Planning 
for the Future 
Core Strategy and Urban Core Plan for 
Gateshead and Newcastle upon Tyne
2010-2030
Adopted March 2015

**[2] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.1 (city: newcastle, score 0.8764)**
> Planning 
for the Future 
Core Strategy and Urban Core Plan for 
Gateshead and Newcastle upon Tyne
2010-2030
Adopted March 2015

**[3] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.2 (city: newcastle, score 0.8426)**
> 2
Planning for the Future Core Strategy and Urban Core Plan was adopted by 
Newcastle and Gateshead Council on 26 March 2015.

**[4] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.2 (city: newcastle, score 0.8425)**
> 2
Planning for the Future Core Strategy and Urban Core Plan was adopted by 
Newcastle and Gateshead Council on 26 March 2015.

**[5] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.43 (city: newcastle, score 0.8185)**
> delay, and where necessary use the guidance in the NPPF to determine  
 applications.
5.6  The Spatial Strategy positively seeks opportunities to meet the 
development needs of Gateshead and Ne
wcastle. The Urban Core (Policy 
CS2 and Section 4) will remain the strategic priority for development in 
Gateshead and Newcastle, to ensure it fulfils its potential in contributing 
to economic prosperity

**[6] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.43 (city: newcastle, score 0.8185)**
> delay, and where necessary use the guidance in the NPPF to determine  
 applications.
5.6  The Spatial Strategy positively seeks opportunities to meet the 
development needs of Gateshead and Ne
wcastle. The Urban Core (Policy 
CS2 and Section 4) will remain the strategic priority for development in 
Gateshead and Newcastle, to ensure it fulfils its potential in contributing 
to economic prosperity

**[7] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.294 (city: newcastle, score 0.8093)**
> The following policies from the Gateshead Unitary Development Plan (UDP) 
(Saved 2010) (column 1) will be superseded by policies in the Core Strategy and 
Urban Core Plan (column 2).

**[8] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.294 (city: newcastle, score 0.8093)**
> The following policies from the Gateshead Unitary Development Plan (UDP) 
(Saved 2010) (column 1) will be superseded by policies in the Core Strategy and 
Urban Core Plan (column 2).

### Rubric (enter in the Evaluate page for `NEW-ST-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NEW-PC-02 — BASELINE

**City:** newcastle | **Category:** policy_compliance | **Difficulty:** medium

**Task:** A developer proposes a major residential scheme in Newcastle with no affordable housing contribution, citing viability. What does the Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030 require for affordable housing, and under what circumstances can the requirement be reduced? Cite the specific policy.

**Expected policies (check these in the source PDF):** Policy CS11 — source: `Newcastle_Gateshead_CSUCP_2010-2030.pdf`

### Output (baseline)

In the context of the proposed major residential scheme in Newcastle, the relevant policy regarding affordable housing is outlined in the **Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030**. Specifically, Policy CS14 addresses affordable housing provision.

### Policy CS14: Affordable Housing

Policy CS14 states that new residential developments should provide a proportion of affordable housing. The standard requirement is for 10% of the total number of dwellings to be affordable housing on sites of 15 or more dwellings. This is in line with the overarching aim to ensure that a mix of housing types is available to meet the needs of the community.

### Circumstances for Reducing Affordable Housing Contributions

The policy does allow for flexibility in the affordable housing requirement under certain circumstances. According to the policy, the affordable housing contribution can be reduced if it can be demonstrated that:

1. **Viability Issues**: The developer must provide robust evidence that the scheme is not viable with the full affordable housing contribution. This typically involves a viability assessment that considers the costs of development, including land acquisition, construction, and other associated costs, against the expected revenue from sales or rentals.

2. **Site-Specific Constraints**: If there are specific constraints related to the site that significantly impact the viability of the development, such as abnormal costs associated with remediation, infrastructure requirements, or other factors that would affect the financial feasibility of including affordable housing.

3. **Market Conditions**: Changes in market conditions that affect the demand and pricing of housing can also be a valid reason for reducing the affordable housing requirement. This would need to be substantiated with current market data.

### Conclusion

In summary, while the Core Strategy and Urban Core Plan for Gateshead and Newcastle sets a clear expectation for affordable housing contributions, it does provide a mechanism for reduction based on viability assessments and site-specific circumstances. The developer will need to submit a detailed viability assessment to justify any reduction in the affordable housing requirement, in accordance with Policy CS14. It is essential that this assessment is transparent and robust to ensure that the local planning authority can adequately evaluate the claims made by the developer. 

For further guidance, the developer should also refer to the **National Planning Policy Framework (NPPF)**, particularly paragraph 57, which emphasizes the importance of viability in planning decisions, and the **Planning Practice Guidance (PPG)**, which provides additional context on assessing viability.

### Rubric (enter in the Evaluate page for `NEW-PC-02` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NEW-PC-02 — RAG

**City:** newcastle | **Category:** policy_compliance | **Difficulty:** medium

**Task:** A developer proposes a major residential scheme in Newcastle with no affordable housing contribution, citing viability. What does the Core Strategy and Urban Core Plan for Gateshead and Newcastle 2010-2030 require for affordable housing, and under what circumstances can the requirement be reduced? Cite the specific policy.

**Expected policies (check these in the source PDF):** Policy CS11 — source: `Newcastle_Gateshead_CSUCP_2010-2030.pdf`

### Output (rag)

The Core Strategy and Urban Core Plan for Gateshead and Newcastle upon Tyne (2010-2030) outlines specific requirements for affordable housing in the region. While the provided extracts do not explicitly detail the affordable housing policy or the circumstances under which the requirement can be reduced, they do indicate a strategic approach to housing provision.

From the context, it is clear that there is an emphasis on increasing the residential population and providing a broader range of housing options (Extract 5 and Extract 7). However, the specific policy regarding affordable housing contributions is not directly mentioned in the extracts provided.

In general UK planning policy, particularly as outlined in the National Planning Policy Framework (NPPF), affordable housing contributions are typically required unless a developer can demonstrate that such contributions would make a scheme unviable. This is often assessed through a viability assessment, which must be robust and transparent.

Given the lack of specific details in the provided extracts, I would recommend consulting the full Core Strategy document, particularly the sections that deal with affordable housing policy, to find the exact requirements and any provisions for reducing those requirements based on viability assessments. 

In summary, while the Core Strategy emphasizes the need for a range of housing types, including affordable housing, the specific policy details and conditions for reducing contributions are not included in the extracts provided. Therefore, further investigation into the complete document is necessary to obtain the precise policy framework regarding affordable housing contributions.

### Retrieved context (8 chunks — verify citations against these)

**[1] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.1 (city: newcastle, score 0.7832)**
> Planning 
for the Future 
Core Strategy and Urban Core Plan for 
Gateshead and Newcastle upon Tyne
2010-2030
Adopted March 2015

**[2] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.1 (city: newcastle, score 0.7832)**
> Planning 
for the Future 
Core Strategy and Urban Core Plan for 
Gateshead and Newcastle upon Tyne
2010-2030
Adopted March 2015

**[3] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.43 (city: newcastle, score 0.7798)**
> delay, and where necessary use the guidance in the NPPF to determine  
 applications.
5.6  The Spatial Strategy positively seeks opportunities to meet the 
development needs of Gateshead and Ne
wcastle. The Urban Core (Policy 
CS2 and Section 4) will remain the strategic priority for development in 
Gateshead and Newcastle, to ensure it fulfils its potential in contributing 
to economic prosperity

**[4] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.43 (city: newcastle, score 0.7798)**
> delay, and where necessary use the guidance in the NPPF to determine  
 applications.
5.6  The Spatial Strategy positively seeks opportunities to meet the 
development needs of Gateshead and Ne
wcastle. The Urban Core (Policy 
CS2 and Section 4) will remain the strategic priority for development in 
Gateshead and Newcastle, to ensure it fulfils its potential in contributing 
to economic prosperity

**[5] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.47 (city: newcastle, score 0.7796)**
> 6.8  There is potential to significantly increase the residential population 
by providing a br
oader range of housing including conversion of upper 
floors in the Urban Core to meet market demands. In Gateshead the 
Exemplar Neighbourhood will be a major new residential area providing 
family homes. In Newcastle we will support housing as part of mixed- 
use schemes. Science Central should provid

**[6] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.47 (city: newcastle, score 0.7796)**
> 6.8  There is potential to significantly increase the residential population 
by providing a br
oader range of housing including conversion of upper 
floors in the Urban Core to meet market demands. In Gateshead the 
Exemplar Neighbourhood will be a major new residential area providing 
family homes. In Newcastle we will support housing as part of mixed- 
use schemes. Science Central should provid

**[7] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.56 (city: newcastle, score 0.7795)**
> 8.5  Strategically we are seeking to provide the homes we need in a r ange 
of locations to offer choice across Gateshead and Newcastle. Whilst the 
majority of housing will be located in the Neighbourhood Area it will not 
be possible to accommodate all of the growth there, or in the Urban Core, 
and therefore other locations have been allocated.
8.6  Allowing limited new housing development in t

**[8] Newcastle_Gateshead_CSUCP_2010-2030.pdf p.56 (city: newcastle, score 0.7795)**
> 8.5  Strategically we are seeking to provide the homes we need in a r ange 
of locations to offer choice across Gateshead and Newcastle. Whilst the 
majority of housing will be located in the Neighbourhood Area it will not 
be possible to accommodate all of the growth there, or in the Urban Core, 
and therefore other locations have been allocated.
8.6  Allowing limited new housing development in t

### Rubric (enter in the Evaluate page for `NEW-PC-02` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NOT-SC-01 — BASELINE

**City:** nottingham | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy DE1 of the Nottingham Land and Planning Policies Document (Local Plan Part 2) means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy DE1 — source: `Nottingham_LAPP_2020.pdf`

### Output (baseline)

**Summary of Policy DE1: Design of New Development in Nottingham**

Dear Residents,

We want to take a moment to explain what Policy DE1 from the Nottingham Land and Planning Policies Document (Local Plan Part 2) means for the design of new developments in our neighbourhood. This policy is important because it sets out the expectations for how new buildings and spaces should look and feel, ensuring they contribute positively to our community.

**Key Points of Policy DE1:**

1. **High-Quality Design**: The policy emphasizes that all new developments must be of high quality. This means that buildings should not only be functional but also visually appealing and well-constructed. The aim is to create spaces that residents can be proud of.

2. **Contextual Fit**: New developments should respect and enhance the character of the surrounding area. This involves considering the local architecture, materials, and the overall environment. For example, if your neighbourhood has traditional brick houses, new buildings should reflect that style rather than introducing starkly modern designs that clash with the existing character.

3. **Sustainability**: Policy DE1 encourages sustainable design practices. This includes using materials and construction methods that are environmentally friendly, as well as incorporating features that reduce energy consumption. This is not only good for the planet but can also lead to lower utility bills for residents.

4. **Accessibility and Inclusivity**: The policy highlights the importance of making sure that new developments are accessible to everyone, including people with disabilities. This means considering things like wheelchair access, safe pedestrian pathways, and adequate public transport links.

5. **Public Spaces**: New developments should include well-designed public spaces that encourage community interaction. This could be parks, squares, or other communal areas where residents can gather, relax, and enjoy their neighbourhood.

6. **Safety and Security**: The design of new developments should also consider safety. This includes ensuring that buildings and public spaces are well-lit and designed to reduce the risk of crime, making residents feel secure in their environment.

7. **Community Involvement**: Finally, the policy encourages developers to engage with local communities during the planning process. This means that residents should have a say in how new developments are designed and how they will impact the neighbourhood.

In summary, Policy DE1 aims to ensure that new developments in Nottingham are not only functional but also enhance the quality of life for residents. By focusing on high-quality design, sustainability, accessibility, and community involvement, we can create a neighbourhood that is attractive, safe, and welcoming for everyone.

If you have any questions or would like to discuss this policy further, please feel free to reach out.

Best regards,

[Your Name]  
[Your Position]  
[Contact Information]  
[Date]

### Rubric (enter in the Evaluate page for `NOT-SC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NOT-SC-01 — RAG

**City:** nottingham | **Category:** stakeholder_communication | **Difficulty:** easy

**Task:** Write a plain-English summary for local residents explaining what Policy DE1 of the Nottingham Land and Planning Policies Document (Local Plan Part 2) means for the design of new development in their neighbourhood.

**Expected policies (check these in the source PDF):** Policy DE1 — source: `Nottingham_LAPP_2020.pdf`

### Output (rag)

**Summary of Policy DE1: Building Design and Use for Local Residents**

Policy DE1 of the Nottingham Land and Planning Policies Document (Local Plan Part 2) outlines important criteria that must be considered when planning new developments in your neighbourhood. Here’s what this means for the design of new buildings:

1. **Design Quality**: All new buildings should be designed to a high standard. This means that they should not only be functional but also visually appealing and in harmony with the surrounding area.

2. **Contextual Fit**: New developments should respect and enhance the character of the local area. This involves considering the existing architectural styles, materials, and the overall environment when designing new buildings.

3. **Sustainability**: The design of new developments should incorporate sustainable practices. This includes energy efficiency, the use of sustainable materials, and designs that promote environmental well-being.

4. **Accessibility**: New buildings must be accessible to everyone, including people with disabilities. This means considering how people will enter and move around the building and ensuring that facilities are available for all.

5. **Community Impact**: The design should take into account how the new development will affect the local community. This includes considering the needs of local residents and how the development will contribute positively to the area.

In summary, Policy DE1 emphasizes that new developments should be well-designed, contextually appropriate, sustainable, accessible, and beneficial to the community. This policy is part of a broader framework that ensures all planning applications are assessed comprehensively, taking into account various relevant policies (as noted in Extracts 1 and 7). 

By adhering to these guidelines, the aim is to create a built environment that enhances the quality of life for all residents in Nottingham.

### Retrieved context (8 chunks — verify citations against these)

**[1] Nottingham_LAPP_2020.pdf p.109 (city: nottingham, score 0.7949)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 101 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy DE1: Building Design and Use 
 
 
1. Planning applications will be considered against the f

**[2] Nottingham_LAPP_2020.pdf p.109 (city: nottingham, score 0.7948)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 101 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy DE1: Building Design and Use 
 
 
1. Planning applications will be considered against the f

**[3] Nottingham_LAPP_2020.pdf p.113 (city: nottingham, score 0.7873)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 105 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy DE2: Context and Place Making 
 
1. Development proposals should help to reinforce and enha

**[4] Nottingham_LAPP_2020.pdf p.113 (city: nottingham, score 0.7871)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 105 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy DE2: Context and Place Making 
 
1. Development proposals should help to reinforce and enha

**[5] Nottingham_LAPP_2020.pdf p.1 (city: nottingham, score 0.7703)**
> Nottingham City  
land and 
planning 
policies 
 
 
 
 
 
Development Plan  
Document 
 
 
 
 
 
 
 
 
 
 
 
 
 
January 2020
Local Plan Part 2

**[6] Nottingham_LAPP_2020.pdf p.1 (city: nottingham, score 0.7703)**
> Nottingham City  
land and 
planning 
policies 
 
 
 
 
 
Development Plan  
Document 
 
 
 
 
 
 
 
 
 
 
 
 
 
January 2020
Local Plan Part 2

**[7] Nottingham_LAPP_2020.pdf p.21 (city: nottingham, score 0.7702)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 13 
January 2020       
 
2.20 Background Papers have been produced, which set out detailed information 
that has been used t

**[8] Nottingham_LAPP_2020.pdf p.21 (city: nottingham, score 0.7701)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 13 
January 2020       
 
2.20 Background Papers have been produced, which set out detailed information 
that has been used t

### Rubric (enter in the Evaluate page for `NOT-SC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NOT-PC-02 — BASELINE

**City:** nottingham | **Category:** policy_compliance | **Difficulty:** medium

**Task:** A developer proposes a major residential scheme in Nottingham with no affordable housing contribution, citing viability. What does the Nottingham Land and Planning Policies Document (Local Plan Part 2) require for affordable housing, and under what circumstances can the requirement be reduced? Cite the specific policy.

**Expected policies (check these in the source PDF):** Policy HO3 — source: `Nottingham_LAPP_2020.pdf`

### Output (baseline)

In Nottingham, the requirements for affordable housing contributions are outlined in the Nottingham Land and Planning Policies Document (Local Plan Part 2). Specifically, Policy 8 of the Local Plan Part 2 addresses affordable housing provision.

**Policy 8: Affordable Housing** states that:

1. **Threshold for Affordable Housing**: The policy generally requires that developments of 10 or more dwellings (or sites of 0.5 hectares or more) should provide a minimum of 20% of the total number of dwellings as affordable housing. This is in line with the overarching aim to ensure that a proportion of new housing is affordable to meet local needs.

2. **Circumstances for Reducing the Requirement**: The policy does allow for flexibility in the affordable housing requirement under certain circumstances. Specifically, if a developer can demonstrate that the provision of affordable housing would make the scheme unviable, they may submit a viability assessment. This assessment must be robust and transparent, and it should be based on the latest market data and development costs. The viability assessment will be scrutinized by the local planning authority, which may consider factors such as:
   - The overall financial viability of the development.
   - The specific costs associated with the development, including site-specific constraints.
   - The current market conditions and demand for housing in the area.

3. **Evidence Requirement**: The developer must provide clear evidence to support any claim of reduced viability. This includes detailed financial appraisals and, where necessary, independent assessments. The local authority may also require the developer to explore alternative funding mechanisms or partnerships that could facilitate the delivery of affordable housing.

4. **Negotiation**: If the viability assessment indicates that the full affordable housing requirement cannot be met, the local authority may negotiate with the developer to determine a feasible level of affordable housing that can be delivered, or consider alternative contributions, such as off-site provision or financial contributions towards affordable housing elsewhere.

In summary, while the Nottingham Local Plan Part 2 sets a clear expectation for affordable housing contributions, it also recognizes that viability issues may necessitate a reduction in these requirements. Developers must provide comprehensive evidence to justify any claims of reduced viability, and the local authority will assess these claims carefully to ensure that the overall objectives of affordable housing provision are met. 

For further reference, you may consult the Nottingham Land and Planning Policies Document (Local Plan Part 2), specifically Policy 8, for detailed guidance on affordable housing requirements and the associated processes for viability assessments.

### Rubric (enter in the Evaluate page for `NOT-PC-02` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## NOT-PC-02 — RAG

**City:** nottingham | **Category:** policy_compliance | **Difficulty:** medium

**Task:** A developer proposes a major residential scheme in Nottingham with no affordable housing contribution, citing viability. What does the Nottingham Land and Planning Policies Document (Local Plan Part 2) require for affordable housing, and under what circumstances can the requirement be reduced? Cite the specific policy.

**Expected policies (check these in the source PDF):** Policy HO3 — source: `Nottingham_LAPP_2020.pdf`

### Output (rag)

The Nottingham Land and Planning Policies Document (Local Plan Part 2) outlines the requirements for affordable housing under Policy HO3. According to this policy, planning permission for new residential developments, including conversions, will be granted subject to specific affordable housing targets, where viable (Extract 1 and Extract 2). 

The term "where viable" indicates that the affordable housing requirement can be reduced if the developer can demonstrate that the provision of affordable housing would render the development unviable. This is further supported by the context provided in Extract 3, which mentions that affordable housing supply is delivered through various mechanisms, including Section 106 contributions. This implies that if a developer can substantiate their claim of viability issues, they may negotiate a lower affordable housing contribution.

However, it is crucial to note that any reduction in the affordable housing requirement must be justified with robust evidence demonstrating that the development's financial viability is compromised by the inclusion of affordable housing. The Local Plan emphasizes that all policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core Strategy, and no policy should be applied in isolation (Extract 1, Extract 5). Therefore, the developer's claim must be carefully assessed against the broader planning context and policies.

In summary, while the Local Plan Part 2 establishes a clear expectation for affordable housing contributions, it allows for flexibility based on viability assessments, which must be adequately evidenced by the developer.

### Retrieved context (8 chunks — verify citations against these)

**[1] Nottingham_LAPP_2020.pdf p.95 (city: nottingham, score 0.8316)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 87 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy HO3: Affordable Housing  
 
1. Planning permission for new residential developments includin

**[2] Nottingham_LAPP_2020.pdf p.95 (city: nottingham, score 0.8315)**
> All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 87 
Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
January 2020       
 
Policy HO3: Affordable Housing  
 
1. Planning permission for new residential developments includin

**[3] Nottingham_LAPP_2020.pdf p.96 (city: nottingham, score 0.798)**
> Section 4: Development Management Policies – Places for People 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
 
88 
 
 
4.29 Affordable housing supply is delivered through a range of mechanisms of which 
Section 106 contributions are one. The 

**[4] Nottingham_LAPP_2020.pdf p.96 (city: nottingham, score 0.798)**
> Section 4: Development Management Policies – Places for People 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
 
88 
 
 
4.29 Affordable housing supply is delivered through a range of mechanisms of which 
Section 106 contributions are one. The 

**[5] Nottingham_LAPP_2020.pdf p.199 (city: nottingham, score 0.7964)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
January 2020       
 191 
6.32  The Development Principles set out the range of acceptable uses for each site. Whilst the 
p

**[6] Nottingham_LAPP_2020.pdf p.199 (city: nottingham, score 0.7964)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
January 2020       
 191 
6.32  The Development Principles set out the range of acceptable uses for each site. Whilst the 
p

**[7] Nottingham_LAPP_2020.pdf p.195 (city: nottingham, score 0.796)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
January 2020       
 187 
 
Table 6: Housing Requirements for Nottingham City  
 
2011 – 18 Core Strategy Requirement 
 
5,3

**[8] Nottingham_LAPP_2020.pdf p.195 (city: nottingham, score 0.796)**
> Nottingham City Council 
Local Plan Part 2 - Land and Planning Policies 
All policies should be read in conjunction with the Local Plan Part 1 – Nottingham City Aligned Core 
Strategy. No policy should be applied in isolation, account will be taken of all relevant policies. 
January 2020       
 187 
 
Table 6: Housing Requirements for Nottingham City  
 
2011 – 18 Core Strategy Requirement 
 
5,3

### Rubric (enter in the Evaluate page for `NOT-PC-02` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## PLY-ST-01 — BASELINE

**City:** plymouth | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Plymouth and South West Devon Joint Local Plan was adopted in 2019, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (baseline)

As an experienced UK planning consultant, I can provide a detailed analysis of how the December 2024 revisions to the National Planning Policy Framework (NPPF) may interact with the Plymouth and South West Devon Joint Local Plan (JLP), which was adopted in 2019. The key areas of potential conflict or supersession include the introduction of grey belts, mandatory housing targets, and amendments to affordable housing policies.

### 1. Grey Belt Designation

**NPPF December 2024 Revision:**
The introduction of grey belts aims to provide a new layer of protection for areas that are not designated as green belts but still require safeguarding from inappropriate development. This policy seeks to balance development needs with environmental and social considerations.

**Impact on the JLP:**
The JLP does not currently incorporate a grey belt designation, as it was adopted prior to this policy change. The introduction of grey belts may create tension in areas where the JLP has identified land for development that could now fall under grey belt protections. This could lead to challenges in delivering the housing and employment targets set out in the JLP, particularly in areas where development was anticipated to occur.

### 2. Mandatory Housing Targets

**NPPF December 2024 Revision:**
The revised NPPF introduces mandatory housing targets that local authorities must meet, which are based on local housing needs assessments. This is a shift from the previous framework, which allowed for more discretion in setting housing targets.

**Impact on the JLP:**
The JLP sets out a housing requirement based on the evidence available at the time of its adoption. If the mandatory targets established by the revised NPPF exceed the housing numbers in the JLP, this could create a significant conflict. The local authorities may be required to undertake a review of the JLP to align with the new targets, potentially leading to increased pressure for housing development in areas that were previously considered sufficient under the JLP's policies.

### 3. Affordable Housing Amendments

**NPPF December 2024 Revision:**
The December 2024 revision includes changes to the definitions and thresholds for affordable housing, emphasizing the need for a greater proportion of affordable homes in new developments. This includes a focus on the delivery of affordable housing that meets local needs, including social rent and affordable rent.

**Impact on the JLP:**
The JLP includes specific policies regarding affordable housing, including thresholds for when affordable housing contributions are required. If the new NPPF policies mandate higher percentages of affordable housing or lower thresholds for contributions, this could necessitate a review of the JLP’s affordable housing policies. Local authorities may face challenges in meeting these new requirements, particularly in areas where viability assessments previously justified lower contributions.

### Conclusion

In summary, the December 2024 revisions to the NPPF introduce significant changes that may supersede or create tension with the Plymouth and South West Devon Joint Local Plan. The introduction of grey belts could limit development opportunities, mandatory housing targets may require a review of housing numbers, and amendments to affordable housing policies could necessitate changes to existing thresholds and contributions. 

Local authorities will need to assess these changes carefully and consider undertaking a review of the JLP to ensure compliance with the revised NPPF, while also balancing local needs and development aspirations. It is advisable for the authorities to engage with stakeholders and the community to navigate these changes effectively.

### Rubric (enter in the Evaluate page for `PLY-ST-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## PLY-ST-01 — RAG

**City:** plymouth | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Plymouth and South West Devon Joint Local Plan was adopted in 2019, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (rag)

The provided context from the Plymouth and South West Devon Joint Local Plan (JLP) does not contain specific details regarding the policy areas that may be affected by the changes introduced in the December 2024 revision of the National Planning Policy Framework (NPPF), such as the introduction of grey belts, mandatory housing targets, and amendments to affordable housing policies. 

However, I can provide a professional analysis based on my knowledge of UK planning policy and the implications of the NPPF revisions:

1. **Grey Belt Designation**: The introduction of grey belts in the NPPF aims to provide a new layer of protection for certain areas, potentially affecting the spatial strategy outlined in the JLP. The JLP's spatial strategy (as indicated in Extract 5) may need to be reassessed to align with the new grey belt designations, particularly if they overlap with areas identified for growth or development.

2. **Mandatory Housing Targets**: The NPPF's introduction of mandatory housing targets could create tension with the JLP's existing housing policies. The JLP outlines a strategic approach to housing delivery, but if the mandatory targets set by the NPPF exceed the planned housing trajectory in the JLP (as suggested in Extract 7), this could necessitate a review of the JLP to ensure compliance with national policy.

3. **Affordable Housing Amendments**: Changes to affordable housing requirements in the NPPF may conflict with the JLP's existing policies on affordable housing provision. If the NPPF mandates higher percentages of affordable housing or different definitions of affordability, the JLP may need to be updated to reflect these changes, particularly in the context of the housing strategy for Plymouth and surrounding areas (as referenced in Extract 5).

In summary, while the context does not provide specific references to these policy areas, the potential conflicts and tensions between the JLP and the December 2024 NPPF revisions are evident based on the overarching themes of housing delivery and spatial planning. A thorough review of the JLP in light of the new NPPF policies will be necessary to ensure alignment and compliance.

### Retrieved context (8 chunks — verify citations against these)

**[1] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.5 (city: plymouth, score 0.7863)**
> development plan for Plymouth, South Hams and West Devon. 
1.3 The JLP excludes policies for Dartmoor National Park Authority. This is because 
the National Park Authority is preparing a separate local plan. However both plans 
will be based on joint evidence. 
Why a joint local plan? 
1.4 The Localism Act requires local planning authorities (LPAs) to cooperate closely 
with neighbouring authoriti

**[2] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.5 (city: plymouth, score 0.7863)**
> development plan for Plymouth, South Hams and West Devon. 
1.3 The JLP excludes policies for Dartmoor National Park Authority. This is because 
the National Park Authority is preparing a separate local plan. However both plans 
will be based on joint evidence. 
Why a joint local plan? 
1.4 The Localism Act requires local planning authorities (LPAs) to cooperate closely 
with neighbouring authoriti

**[3] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.5 (city: plymouth, score 0.7828)**
> 1 Introduction 
What is the Plymouth and South West Devon Joint Local Plan? 
1.1 The Joint Local Plan (JLP) is part of a ground-breaking strategic planning 
process for Plymouth and South West Devon which looks ahead to 2034. It sets a 
shared direction of travel for the long term future of the area, within the context of 
wider integrated strategic plans. In this respect it integrates with and co

**[4] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.5 (city: plymouth, score 0.7828)**
> 1 Introduction 
What is the Plymouth and South West Devon Joint Local Plan? 
1.1 The Joint Local Plan (JLP) is part of a ground-breaking strategic planning 
process for Plymouth and South West Devon which looks ahead to 2034. It sets a 
shared direction of travel for the long term future of the area, within the context of 
wider integrated strategic plans. In this respect it integrates with and co

**[5] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.3 (city: plymouth, score 0.7614)**
> Plymouth and South West Devon Joint Local Plan 
1 Introduction 3 
2 Vision 8 
3 Spatial Strategy 13 
4 Strategy for Plymouth Policy Area 57 
a. Plymouth's strategic role 57 
b. Plymouth's Growth Areas 65 
i. The City Centre and Waterfront Growth Area 67 
ii. The Derriford and Northern Corridor Growth Area 118 
iii. The Eastern Corridor Growth Area 145 
c. Other areas and sites 165 
5 Strategy for 

**[6] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.3 (city: plymouth, score 0.7614)**
> Plymouth and South West Devon Joint Local Plan 
1 Introduction 3 
2 Vision 8 
3 Spatial Strategy 13 
4 Strategy for Plymouth Policy Area 57 
a. Plymouth's strategic role 57 
b. Plymouth's Growth Areas 65 
i. The City Centre and Waterfront Growth Area 67 
ii. The Derriford and Northern Corridor Growth Area 118 
iii. The Eastern Corridor Growth Area 145 
c. Other areas and sites 165 
5 Strategy for 

**[7] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.328 (city: plymouth, score 0.7596)**
> 2018 
Plymouth City 
Council, South 
Hams District 
Joint Local Plan Area 
Housing Trajectory 
March 2017 Monitoring 
TP3J 
Council and West 
Devon Borough 
Council 
Point, incorporating 
proposed Main 
Modifications 
October 
2018 
Plymouth City 
Council, South 
Hams District 
Plymouth Policy Area 
Housing Trajectory 
March 2017 Monitoring 
TP3K 
Council and West 
Devon Borough 
Council 
Point, i

**[8] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.328 (city: plymouth, score 0.7595)**
> 2018 
Plymouth City 
Council, South 
Hams District 
Joint Local Plan Area 
Housing Trajectory 
March 2017 Monitoring 
TP3J 
Council and West 
Devon Borough 
Council 
Point, incorporating 
proposed Main 
Modifications 
October 
2018 
Plymouth City 
Council, South 
Hams District 
Plymouth Policy Area 
Housing Trajectory 
March 2017 Monitoring 
TP3K 
Council and West 
Devon Borough 
Council 
Point, i

### Rubric (enter in the Evaluate page for `PLY-ST-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## PLY-PC-01 — BASELINE

**City:** plymouth | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Plymouth city centre comply with the housing policies of the Plymouth and South West Devon Joint Local Plan and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy SPT3, Policy DEV7, Policy DEV10, NPPF para 11, NPPF para 120 — source: `Plymouth_SWDevon_Joint_Local_Plan_2019.pdf`

### Output (baseline)

To assess whether the proposed 80-unit residential development on a brownfield site in Plymouth city centre complies with the housing policies of the Plymouth and South West Devon Joint Local Plan (JLP) and the National Planning Policy Framework (NPPF) December 2024, we need to consider several key policies and principles.

### 1. **Plymouth and South West Devon Joint Local Plan (JLP)**

#### **Policy SPT1: Sustainable Development**
This policy emphasizes the need for sustainable development that meets the needs of the present without compromising the ability of future generations to meet their own needs. The proposed development should demonstrate how it contributes to economic, social, and environmental sustainability.

#### **Policy SPT2: Sustainable Linked Communities**
This policy supports development that enhances the sustainability of communities. Given that the site is in the city centre, it is likely to be well-connected and accessible, which aligns with this policy.

#### **Policy H1: Housing Supply**
This policy outlines the need for a sufficient supply of housing to meet local needs. The JLP sets a target for new homes, and the proposed 80 units would contribute positively to this target, particularly in a city centre location where there is a demand for housing.

#### **Policy H2: Affordable Housing**
This policy requires a proportion of new housing to be affordable. Depending on the size and tenure of the proposed development, it will need to comply with the affordable housing requirements set out in the JLP, which typically requires 20% affordable housing on developments of 10 or more units.

#### **Policy H3: Housing Mix**
This policy encourages a mix of housing types and sizes to meet the diverse needs of the community. The proposed development should consider the local housing needs assessment to ensure it provides a suitable mix of units.

### 2. **National Planning Policy Framework (NPPF) December 2024**

#### **Paragraph 11: Presumption in Favour of Sustainable Development**
The NPPF promotes a presumption in favour of sustainable development, which is particularly relevant for brownfield sites. The development should be assessed against the benefits it brings, including the efficient use of land and contribution to housing supply.

#### **Paragraph 78: Housing in Rural Areas**
While this paragraph primarily addresses rural areas, it emphasizes the importance of delivering housing in sustainable locations. The city centre location of the proposed development aligns with this principle.

#### **Paragraph 92: Planning for Healthy and Safe Communities**
This paragraph highlights the need for developments to create inclusive and safe places. The proposal should consider how it contributes to community well-being, including access to services and facilities.

#### **Paragraph 119: Brownfield Land**
The NPPF encourages the use of brownfield land for development, which is directly relevant to the proposed site. The development should demonstrate how it maximizes the use of previously developed land.

#### **Paragraph 124: Effective Use of Land**
This paragraph stresses the importance of making efficient use of land, particularly in urban areas. The proposed development should demonstrate how it optimizes the site’s potential while considering local context and character.

### Conclusion

In summary, the proposed 80-unit residential development on a brownfield site in Plymouth city centre appears to align with several key policies from both the Plymouth and South West Devon Joint Local Plan and the NPPF. Specifically, it supports sustainable development (SPT1), contributes to housing supply (H1), and utilizes brownfield land effectively (NPPF Paragraph 119). However, it must also address affordable housing requirements (H2) and ensure a suitable housing mix (H3).

To ensure full compliance, the development proposal should include a detailed assessment of how it meets these policies, particularly in terms of affordable housing provision and the mix of unit types. Additionally, engagement with local stakeholders and consideration of local community needs will be essential in the planning process.

### Rubric (enter in the Evaluate page for `PLY-PC-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## PLY-PC-01 — RAG

**City:** plymouth | **Category:** policy_compliance | **Difficulty:** medium

**Task:** Does a proposed 80-unit residential development on a brownfield site in Plymouth city centre comply with the housing policies of the Plymouth and South West Devon Joint Local Plan and the NPPF December 2024? Identify which specific policies and paragraphs apply.

**Expected policies (check these in the source PDF):** Policy SPT3, Policy DEV7, Policy DEV10, NPPF para 11, NPPF para 120 — source: `Plymouth_SWDevon_Joint_Local_Plan_2019.pdf`

### Output (rag)

To assess whether a proposed 80-unit residential development on a brownfield site in Plymouth city centre complies with the housing policies of the Plymouth and South West Devon Joint Local Plan and the National Planning Policy Framework (NPPF) December 2024, we can draw on the provided extracts.

### Compliance with Plymouth and South West Devon Joint Local Plan

1. **Policy PLY58**: This policy allocates sites for development in south Plymouth, including the provision of housing. While the specific extract does not detail the exact requirements for residential developments, it emphasizes the need for sustainable linked neighbourhoods and the importance of not having a significant adverse impact on existing infrastructure (Extract 1 and 2). The proposed development should ensure that it aligns with these principles, particularly in terms of sustainability and infrastructure impact.

2. **High Quality Publicly Accessible Greenspace**: According to the extracts (Extract 3 and 4), developments must include the delivery of high-quality publicly accessible greenspace to mitigate the loss of greenspace and enhance the enjoyment of the historic environment. If the proposed residential development does not incorporate such greenspace, it may not fully comply with this requirement.

3. **Transport Assessment and Mitigation**: The development must also include a transport assessment and mitigation measures, particularly in relation to the Victoria interchange (Extract 3 and 4). This is crucial for ensuring that the development does not exacerbate existing transport issues in the area.

4. **Contribution to Strategic Outcomes**: The development should contribute to the overall vision of the plan and meet the strategic outcomes set out for the Eastern Corridor Growth Area (Extract 5 and 6). This means that the proposed development should align with broader planning objectives, such as enhancing local infrastructure and community facilities.

### Compliance with NPPF December 2024

While the specific text of the NPPF December 2024 is not provided in the context, general principles from the NPPF can be applied:

1. **Sustainable Development**: The NPPF emphasizes the need for sustainable development, which includes the provision of housing that meets local needs while ensuring environmental sustainability. The proposed development should demonstrate how it meets these criteria.

2. **Brownfield Development**: The NPPF encourages the use of brownfield sites for new housing developments, which aligns with the proposed site being a brownfield location. This is a positive aspect of the proposal.

3. **Local Housing Needs**: The NPPF stresses the importance of meeting local housing needs, which includes providing a mix of housing types and tenures. The proposed 80 units should be assessed against local housing needs to ensure compliance.

### Conclusion

In summary, the proposed 80-unit residential development on a brownfield site in Plymouth city centre must comply with several key policies from the Plymouth and South West Devon Joint Local Plan, particularly those related to sustainable development, greenspace provision, and transport assessments. Additionally, it should align with the overarching principles of the NPPF regarding sustainable development and local housing needs. 

To ensure full compliance, the development proposal should address the specific requirements outlined in the Joint Local Plan and demonstrate how it contributes to the strategic outcomes of the area.

### Retrieved context (8 chunks — verify citations against these)

**[1] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.168 (city: plymouth, score 0.7907)**
> development of sustainable linked neighbourhoods. 
Proposal Est. of 
housing 
provision / 
Employment 
floorspace 
Policy considerations / things to be 
provided for by the development 
Site 
Policy PLY58 
Site allocations in the south of Plymouth 
The following sites are allocated for development in south Plymouth: 
Medium sized 
food retail store 
Land at St Levan 
Gate, Keyham 
1 a. Upgrading o

**[2] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.168 (city: plymouth, score 0.7907)**
> development of sustainable linked neighbourhoods. 
Proposal Est. of 
housing 
provision / 
Employment 
floorspace 
Policy considerations / things to be 
provided for by the development 
Site 
Policy PLY58 
Site allocations in the south of Plymouth 
The following sites are allocated for development in south Plymouth: 
Medium sized 
food retail store 
Land at St Levan 
Gate, Keyham 
1 a. Upgrading o

**[3] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.174 (city: plymouth, score 0.7801)**
> 4 Strategy for Plymouth Policy Area 
Policy considerations / things to be 
provided for by the development 
Est. of 
housing 
provision / 
Employment 
floorspace 
Proposal Site 
c. Transport assessment and 
mitigation in relation to Victoria 
interchange 
d. Development must include delivery 
of high quality publicly accessible 
greenspace to mitigate for the loss 
of greenspace and provide for 
e

**[4] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.174 (city: plymouth, score 0.7801)**
> 4 Strategy for Plymouth Policy Area 
Policy considerations / things to be 
provided for by the development 
Est. of 
housing 
provision / 
Employment 
floorspace 
Proposal Site 
c. Transport assessment and 
mitigation in relation to Victoria 
interchange 
d. Development must include delivery 
of high quality publicly accessible 
greenspace to mitigate for the loss 
of greenspace and provide for 
e

**[5] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.166 (city: plymouth, score 0.7774)**
> 4 Strategy for Plymouth Policy Area 
4.223 Policy PLY56 identifies six further sites for development within the plan 
period. These sites are expressed in table format as the key requirements relating 
to each proposal can at this stage be expressed in a relatively few points. However, 
each proposal is significant in terms of the contribution that it makes to the overall 
vision of the plan and m

**[6] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.166 (city: plymouth, score 0.7773)**
> 4 Strategy for Plymouth Policy Area 
4.223 Policy PLY56 identifies six further sites for development within the plan 
period. These sites are expressed in table format as the key requirements relating 
to each proposal can at this stage be expressed in a relatively few points. However, 
each proposal is significant in terms of the contribution that it makes to the overall 
vision of the plan and m

**[7] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.132 (city: plymouth, score 0.7759)**
> 4 Strategy for Plymouth Policy Area 
1. Office accommodation is supported on the eastern section of the sites, 
particularly along the frontage of the A386. Provision is made for in the order 
of 18,000 sq.m. (net). 
2. Development will not be permitted which prejudices the viability and vitality 
of other centres in the retail hierarchy including the City Centre or the 
deliverability, viability 

**[8] Plymouth_SWDevon_Joint_Local_Plan_2019.pdf p.132 (city: plymouth, score 0.7759)**
> 4 Strategy for Plymouth Policy Area 
1. Office accommodation is supported on the eastern section of the sites, 
particularly along the frontage of the A386. Provision is made for in the order 
of 18,000 sq.m. (net). 
2. Development will not be permitted which prejudices the viability and vitality 
of other centres in the retail hierarchy including the City Centre or the 
deliverability, viability 

### Rubric (enter in the Evaluate page for `PLY-PC-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SHE-SA-01 — BASELINE

**City:** sheffield | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in Attercliffe, Sheffield, for a residential-led mixed-use development. Identify the relevant policies from the Sheffield Core Strategy and any likely constraints.

**Expected policies (check these in the source PDF):** Policy CS22, Policy CS23, Policy CS24, Policy CS74 — source: `Sheffield_Core_Strategy_2009.pdf`

### Output (baseline)

### Assessment of a 2-Hectare Former Industrial Site in Attercliffe, Sheffield for Residential-Led Mixed-Use Development

#### 1. **Site Context and Overview**
Attercliffe is an area within Sheffield that has historically been industrial but is undergoing significant regeneration. The site in question, being a former industrial site, presents both opportunities and challenges for redevelopment, particularly for a residential-led mixed-use scheme.

#### 2. **Relevant Policies from the Sheffield Core Strategy**
The Sheffield Core Strategy (adopted in 2009) provides the overarching framework for development in Sheffield. Key policies relevant to the proposed development include:

- **Policy CS1: Overall Approach to Development**: This policy promotes sustainable development that meets the needs of the community while enhancing the environment. A residential-led mixed-use development aligns with this approach, particularly if it includes affordable housing and community facilities.

- **Policy CS2: Spatial Strategy**: This policy encourages development in areas that are well-connected and can support sustainable transport. Attercliffe's proximity to public transport links and existing infrastructure supports this policy.

- **Policy CS3: Locations for New Housing**: This policy supports residential development on previously developed land, particularly in urban areas. Given that the site is a former industrial site, it is classified as brownfield land, which is a priority for housing development.

- **Policy CS5: Providing for Housing**: This policy emphasizes the need for a mix of housing types and tenures. A mixed-use development could provide a range of housing options, contributing to the local housing supply.

- **Policy CS6: Economic Development**: While the site is proposed for residential use, the inclusion of commercial or community facilities would align with this policy, promoting local economic growth.

- **Policy CS74: Design Principles**: This policy requires that new developments are of high quality and contribute positively to the local character. Any proposal will need to demonstrate how it enhances the local environment.

#### 3. **Potential Constraints**
While the site presents opportunities, several constraints must be considered:

- **Contamination**: As a former industrial site, there may be land contamination issues that need to be addressed through appropriate remediation measures. This is critical to ensure the safety of future residents and compliance with environmental regulations.

- **Noise and Air Quality**: Proximity to existing industrial uses and transport routes may raise concerns regarding noise and air quality. An assessment will be necessary to determine the impact on residential amenity and to identify mitigation measures.

- **Flood Risk**: Depending on the site's location relative to water bodies, there may be flood risk considerations. A flood risk assessment will be required to ensure compliance with the National Planning Policy Framework (NPPF) and local flood risk management policies.

- **Infrastructure Capacity**: The local infrastructure, including transport, utilities, and community services, must be assessed to ensure it can accommodate the additional demand from a residential-led development.

- **Heritage Considerations**: If the site is near any designated heritage assets, there may be implications for the design and layout of the development to ensure it preserves the character of the area.

#### 4. **Conclusion**
In summary, the 2-hectare former industrial site in Attercliffe is suitable for a residential-led mixed-use development, aligning with the Sheffield Core Strategy and national planning policies. However, careful consideration of potential constraints, particularly regarding contamination, noise, air quality, flood risk, and infrastructure capacity, will be essential. A comprehensive planning application should include detailed assessments and proposals to address these issues, ensuring that the development contributes positively to the local community and environment. 

Engagement with local stakeholders and the community will also be crucial in shaping a development that meets local needs and aspirations.

### Rubric (enter in the Evaluate page for `SHE-SA-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SHE-SA-01 — RAG

**City:** sheffield | **Category:** site_appraisal | **Difficulty:** hard

**Task:** Assess the suitability of a hypothetical 2-hectare former industrial site in Attercliffe, Sheffield, for a residential-led mixed-use development. Identify the relevant policies from the Sheffield Core Strategy and any likely constraints.

**Expected policies (check these in the source PDF):** Policy CS22, Policy CS23, Policy CS24, Policy CS74 — source: `Sheffield_Core_Strategy_2009.pdf`

### Output (rag)

To assess the suitability of a hypothetical 2-hectare former industrial site in Attercliffe, Sheffield, for a residential-led mixed-use development, we can refer to the relevant policies outlined in the Sheffield Core Strategy and consider potential constraints.

### Relevant Policies

1. **Housing in Attercliffe and Darnall (CS28)**: The Sheffield Core Strategy identifies Attercliffe as a key area for housing development. This policy supports residential development in the area, which aligns with the proposed use of the site for residential-led mixed-use development (Extract 3 and 4).

2. **Jobs and Housing in the Sheaf Valley and Neighbouring Areas (CS30)**: This policy emphasizes the importance of integrating housing with job opportunities, which is relevant for a mixed-use development. The site could potentially accommodate both residential units and commercial spaces, contributing to local employment (Extract 3 and 4).

3. **Transport Investment and Management**: Although not explicitly detailed in the extracts, the mention of transport investment and management in relation to the Meadowhall Centre suggests that accessibility and transport links are important considerations for any development in the area (Extract 1 and 2). Ensuring good transport links will be crucial for the success of a mixed-use development.

### Likely Constraints

1. **Site History and Remediation**: As a former industrial site, there may be contamination issues that need to be addressed before development can proceed. This could involve significant remediation efforts, which can be costly and time-consuming.

2. **Infrastructure Capacity**: The existing infrastructure, including roads, utilities, and public services, must be assessed to determine if it can support the proposed development. The Core Strategy emphasizes the need for transport investment, indicating that current infrastructure may require upgrades (Extract 1 and 2).

3. **Community Impact**: The development should consider the impact on the existing community, including the need for public spaces and amenities. The Core Strategy mentions the importance of improving public realms, which could be a requirement for the development to enhance local quality of life (Extract 7 and 8).

4. **Planning Permissions and Local Consultation**: Any development will need to go through the appropriate planning permissions process, which may involve consultations with local residents and stakeholders. This can sometimes lead to delays or modifications to the proposed plans based on community feedback.

### Conclusion

In summary, the 2-hectare former industrial site in Attercliffe is suitable for a residential-led mixed-use development, supported by policies CS28 and CS30 of the Sheffield Core Strategy. However, potential constraints such as site contamination, infrastructure capacity, community impact, and the planning process must be carefully considered and addressed to ensure a successful development.

### Retrieved context (8 chunks — verify citations against these)

**[1] Sheffield_Core_Strategy_2009.pdf p.175 (city: sheffield, score 0.7318)**
> MeadowhallCentreatWeedonStreet/Carbrook
Developmentbriefs(S/M/L)
Marketingofthelocation(S/M/L)
Transportinvestmentandmanagementincludingtravelplans(S/M/L)
Appendix1:Page139SheffieldCoreStrategy

**[2] Sheffield_Core_Strategy_2009.pdf p.175 (city: sheffield, score 0.7317)**
> MeadowhallCentreatWeedonStreet/Carbrook
Developmentbriefs(S/M/L)
Marketingofthelocation(S/M/L)
Transportinvestmentandmanagementincludingtravelplans(S/M/L)
Appendix1:Page139SheffieldCoreStrategy

**[3] Sheffield_Core_Strategy_2009.pdf p.220 (city: sheffield, score 0.7272)**
> PLD2DA2b3.1,4.1,5.1,5.3,15.3HousinginAttercliffeand
Darnall
CS28
PUD4NW2b3.1,4.1,5.3,15.3HousingintheUpperDon
Valley
CS29
PSV1,2,3,4SW1a,b,c,SW2a1.1,1.2,1.6,4.2JobsandHousingintheSheaf
ValleyandNeighbouring
Areas
CS30
PSW1SW5b4.1,14.1,14.2,15.2HousingintheSouth-West
Area
CS31
Appendix4:Page184SheffieldCoreStrategy

**[4] Sheffield_Core_Strategy_2009.pdf p.220 (city: sheffield, score 0.7272)**
> PLD2DA2b3.1,4.1,5.1,5.3,15.3HousinginAttercliffeand
Darnall
CS28
PUD4NW2b3.1,4.1,5.3,15.3HousingintheUpperDon
Valley
CS29
PSV1,2,3,4SW1a,b,c,SW2a1.1,1.2,1.6,4.2JobsandHousingintheSheaf
ValleyandNeighbouring
Areas
CS30
PSW1SW5b4.1,14.1,14.2,15.2HousingintheSouth-West
Area
CS31
Appendix4:Page184SheffieldCoreStrategy

**[5] Sheffield_Core_Strategy_2009.pdf p.226 (city: sheffield, score 0.7242)**
> ● ● ●HousingintheCityCentreCS27
●● ●HousinginAttercliffeandDarnallCS28
●● ●HousingintheUpperDonValleyCS29
Appendix5:Page190SheffieldCoreStrategy

**[6] Sheffield_Core_Strategy_2009.pdf p.226 (city: sheffield, score 0.7239)**
> ● ● ●HousingintheCityCentreCS27
●● ●HousinginAttercliffeandDarnallCS28
●● ●HousingintheUpperDonValleyCS29
Appendix5:Page190SheffieldCoreStrategy

**[7] Sheffield_Core_Strategy_2009.pdf p.190 (city: sheffield, score 0.7223)**
> reviews(S/M/L)
Developmentproposals(S/M/L)
Marketingtoraisetheprofileofthearea.Fundingistheremitof
CreativeSheffield(S/M/L)
†
Improvedpublicrealm,particularlytheupgradingofEllesmereGreen
publicspace(£790,000fundingistobeprovidedbyBurngreaveNew
Deal).IftheTescodevelopmentgoesaheadthiswillprovideatleast
Appendix1:Page154SheffieldCoreStrategy

**[8] Sheffield_Core_Strategy_2009.pdf p.190 (city: sheffield, score 0.7221)**
> reviews(S/M/L)
Developmentproposals(S/M/L)
Marketingtoraisetheprofileofthearea.Fundingistheremitof
CreativeSheffield(S/M/L)
†
Improvedpublicrealm,particularlytheupgradingofEllesmereGreen
publicspace(£790,000fundingistobeprovidedbyBurngreaveNew
Deal).IftheTescodevelopmentgoesaheadthiswillprovideatleast
Appendix1:Page154SheffieldCoreStrategy

### Rubric (enter in the Evaluate page for `SHE-SA-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SHE-ST-01 — BASELINE

**City:** sheffield | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Sheffield Core Strategy was adopted in 2009, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (baseline)

As an experienced UK planning consultant, I can provide a detailed analysis of how the December 2024 revisions to the National Planning Policy Framework (NPPF) may supersede or create tension with the Sheffield Core Strategy, which was adopted in 2009. The key areas of concern include the grey belt designation, mandatory housing targets, and amendments to affordable housing policies.

### 1. Grey Belt Designation

**NPPF Changes:**
The December 2024 revision introduces a new concept of "grey belt," which is intended to provide a more flexible approach to land use, particularly in urban areas where there is pressure for development. This designation allows for a reassessment of land that may not meet the strict criteria of the traditional Green Belt but still serves a purpose in terms of environmental protection and urban containment.

**Tension with Sheffield Core Strategy:**
The Sheffield Core Strategy, while recognizing the importance of green spaces and the need to protect the Green Belt, may not have provisions that align with the new grey belt concept. The Core Strategy's policies may be more rigid in terms of land use, potentially limiting the ability to adapt to the new framework that encourages development in grey belt areas. This could lead to conflicts in planning decisions, particularly in areas where there is a need for housing or economic development.

### 2. Mandatory Housing Targets

**NPPF Changes:**
The December 2024 revision establishes mandatory housing targets that local authorities must meet, which are based on a standard methodology that considers local housing needs, demographic changes, and economic factors. This is a shift from the previous approach, which allowed for more local discretion in setting housing targets.

**Tension with Sheffield Core Strategy:**
The Sheffield Core Strategy includes housing targets that were set based on local assessments at the time of its adoption. If the mandatory targets set by the NPPF exceed those in the Core Strategy, Sheffield City Council may face challenges in meeting these new requirements. This could necessitate a review of the Core Strategy to align with the NPPF, potentially leading to conflicts with existing policies and community expectations regarding development.

### 3. Affordable Housing Amendments

**NPPF Changes:**
The December 2024 revision includes amendments to the approach to affordable housing, emphasizing the need for a greater proportion of affordable homes in new developments. It also introduces more stringent requirements for viability assessments, ensuring that affordable housing contributions are not easily dismissed by developers.

**Tension with Sheffield Core Strategy:**
The Sheffield Core Strategy includes specific policies regarding affordable housing, which may not align with the new requirements. If the Core Strategy allows for lower percentages of affordable housing or provides more flexibility for developers to avoid contributions, this could create a significant tension with the NPPF's emphasis on delivering affordable housing. The Council may need to revise its policies to ensure compliance with the NPPF, which could lead to challenges in negotiations with developers and impact the overall delivery of housing in the city.

### Conclusion

In summary, the December 2024 revisions to the NPPF introduce significant changes that may supersede or create tension with the Sheffield Core Strategy. The introduction of the grey belt concept, mandatory housing targets, and stricter affordable housing requirements necessitate a careful review and potential revision of the Core Strategy to ensure alignment with national policy. Sheffield City Council will need to engage in a comprehensive assessment of its planning policies to address these changes effectively and meet the evolving needs of its community.

### Rubric (enter in the Evaluate page for `SHE-ST-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SHE-ST-01 — RAG

**City:** sheffield | **Category:** strategic_analysis | **Difficulty:** hard

**Task:** The Sheffield Core Strategy was adopted in 2009, before the NPPF December 2024 revision. Identify the policy areas where the December 2024 changes (grey belt, mandatory housing targets, affordable housing amendments) supersede or create tension with the adopted plan.

**Expected policies (check these in the source PDF):** NPPF Annex 1 — source: `NPPF_December_2024.pdf`

### Output (rag)

The Sheffield Core Strategy, adopted in 2009, outlines various policies related to housing and land use. However, the recent changes introduced in the National Planning Policy Framework (NPPF) revision of December 2024 may create tensions or supersede certain aspects of the Core Strategy. Here’s a detailed analysis based on the provided context:

1. **Grey Belt Designation**: The Core Strategy does not explicitly mention a "grey belt" designation, which is a new concept introduced in the December 2024 NPPF. This designation typically aims to protect certain areas from development while allowing for some flexibility in land use. The absence of this designation in the Core Strategy could lead to conflicts if the NPPF encourages the identification of grey belt areas that were not previously considered in Sheffield's planning framework.

2. **Mandatory Housing Targets**: The Core Strategy includes a commitment to deliver 2,500 dwellings (up to 50% affordable) from 2008 onward, as noted in the Central Riverside Regeneration Strategy (Extract 5). However, the December 2024 NPPF introduces mandatory housing targets that local authorities must meet. If these targets are higher than what the Core Strategy anticipates, there may be a conflict regarding the adequacy of land supply and the strategies for meeting these targets. The Core Strategy's existing policies (e.g., CS24 on priorities for releasing land for new housing) may need to be revisited to align with the new requirements.

3. **Affordable Housing Amendments**: The Core Strategy's aim to provide up to 50% affordable housing (Extract 5) may also be at odds with any new stipulations in the NPPF regarding affordable housing contributions. If the NPPF introduces stricter definitions or requirements for affordable housing, or if it mandates a different percentage, this could create tension with the existing Core Strategy policies. The Core Strategy does not provide specific percentages or mechanisms for adjusting affordable housing targets in response to changing needs, which may necessitate a review in light of the NPPF changes.

In summary, the key areas of potential conflict or supersession between the Sheffield Core Strategy and the December 2024 NPPF revisions include the introduction of grey belt designations, the establishment of mandatory housing targets, and amendments to affordable housing requirements. The Core Strategy may require updates to ensure compliance with the latest national policies and to effectively address the housing needs of Sheffield.

### Retrieved context (8 chunks — verify citations against these)

**[1] Sheffield_Core_Strategy_2009.pdf p.1 (city: sheffield, score 0.7796)**
> Sheffield Development Framework
Core Strategy
Adopted March 2009
6088 Core Strategy Cover:A4 Cover & Back Spread  6/3/09  16:04  Page 1

**[2] Sheffield_Core_Strategy_2009.pdf p.1 (city: sheffield, score 0.7796)**
> Sheffield Development Framework
Core Strategy
Adopted March 2009
6088 Core Strategy Cover:A4 Cover & Back Spread  6/3/09  16:04  Page 1

**[3] Sheffield_Core_Strategy_2009.pdf p.3 (city: sheffield, score 0.7671)**
> Sheffield Development Framework
Core Strategy
Adopted by the City Council on 4th March 2009
Development Services
Sheffield City Council
Howden House
1 Union Street
Sheffield
S1 2SH
Sheffield Core Strategy

**[4] Sheffield_Core_Strategy_2009.pdf p.3 (city: sheffield, score 0.7671)**
> Sheffield Development Framework
Core Strategy
Adopted by the City Council on 4th March 2009
Development Services
Sheffield City Council
Howden House
1 Union Street
Sheffield
S1 2SH
Sheffield Core Strategy

**[5] Sheffield_Core_Strategy_2009.pdf p.184 (city: sheffield, score 0.7609)**
> 2001-2011
SheffieldCentralRiversideRegenerationStrategy(S*/M/L)
LocalHousingCompany–SheffieldpilotapprovedbyGovernment
–aimistodeliver2,500dwellings(upto50%affordable)from2008
onwardsovera5-10yearperiod(S*/M/L)
Appendix1:Page148SheffieldCoreStrategy

**[6] Sheffield_Core_Strategy_2009.pdf p.184 (city: sheffield, score 0.7609)**
> 2001-2011
SheffieldCentralRiversideRegenerationStrategy(S*/M/L)
LocalHousingCompany–SheffieldpilotapprovedbyGovernment
–aimistodeliver2,500dwellings(upto50%affordable)from2008
onwardsovera5-10yearperiod(S*/M/L)
Appendix1:Page148SheffieldCoreStrategy

**[7] Sheffield_Core_Strategy_2009.pdf p.237 (city: sheffield, score 0.7526)**
> CS24
●PrioritiesforReleasingLandforNewHousing
CS25
●EfficientUseofHousingLandandAccessibility
CS26
Appendix7:Page201SheffieldCoreStrategy

**[8] Sheffield_Core_Strategy_2009.pdf p.237 (city: sheffield, score 0.752)**
> CS24
●PrioritiesforReleasingLandforNewHousing
CS25
●EfficientUseofHousingLandandAccessibility
CS26
Appendix7:Page201SheffieldCoreStrategy

### Rubric (enter in the Evaluate page for `SHE-ST-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SOU-ES-01 — BASELINE

**City:** southampton | **Category:** evidence_synthesis | **Difficulty:** medium

**Task:** Summarise the overall spatial strategy and housing requirement set out in the Southampton Core Strategy (amended 2015), citing the key strategic policies (Policy CS4, Policy CS5, Policy CS16 where relevant).

**Expected policies (check these in the source PDF):** Policy CS4, Policy CS5, Policy CS16 — source: `Southampton_Core_Strategy_2015_amended.pdf`

### Output (baseline)

The Southampton Core Strategy (amended 2015) outlines a comprehensive spatial strategy aimed at guiding the city’s development and addressing its housing needs. The strategy is underpinned by several key policies that collectively aim to promote sustainable growth, enhance the urban environment, and meet the housing requirements of the city.

### Overall Spatial Strategy

The spatial strategy for Southampton is focused on promoting sustainable development that supports economic growth while ensuring the efficient use of land and resources. The strategy emphasizes the importance of urban regeneration, particularly in the city centre and along key transport corridors, to create vibrant, mixed-use communities. The Core Strategy aims to balance the need for housing, employment, and infrastructure, while also enhancing the quality of life for residents.

### Housing Requirement

The Core Strategy sets a clear housing requirement to address the needs of the growing population. The key policies relevant to housing are as follows:

1. **Policy CS4 - Housing Delivery**: This policy establishes the overall housing requirement for Southampton, which is set at a minimum of 13,000 new homes to be delivered between 2006 and 2026. The policy emphasizes the need for a mix of housing types and tenures to meet the diverse needs of the population, including affordable housing. The delivery of these homes is to be supported by appropriate infrastructure and services.

2. **Policy CS5 - Southampton’s Housing Supply**: This policy outlines the approach to delivering the housing requirement identified in Policy CS4. It identifies specific sites and areas for development, including brownfield sites and areas for regeneration. The policy encourages the efficient use of land, prioritizing previously developed land to minimize the impact on greenfield sites. It also highlights the importance of working with developers and stakeholders to ensure that housing delivery is aligned with local needs and infrastructure capacity.

3. **Policy CS16 - Housing Mix and Type**: This policy focuses on the need for a diverse range of housing types and sizes to cater to different demographics, including families, young professionals, and older residents. It promotes the provision of affordable housing and encourages the development of specialist housing for vulnerable groups. The policy aims to ensure that new developments contribute to a balanced and sustainable community.

### Conclusion

In summary, the Southampton Core Strategy (amended 2015) establishes a robust framework for spatial planning and housing delivery in the city. Through Policies CS4, CS5, and CS16, the strategy sets a clear housing requirement of 13,000 new homes, promotes sustainable urban regeneration, and emphasizes the need for a diverse housing mix. This approach is designed to support the city’s growth while enhancing the quality of life for its residents and ensuring that development is sustainable and well-integrated with existing infrastructure.

### Rubric (enter in the Evaluate page for `SOU-ES-01` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SOU-ES-01 — RAG

**City:** southampton | **Category:** evidence_synthesis | **Difficulty:** medium

**Task:** Summarise the overall spatial strategy and housing requirement set out in the Southampton Core Strategy (amended 2015), citing the key strategic policies (Policy CS4, Policy CS5, Policy CS16 where relevant).

**Expected policies (check these in the source PDF):** Policy CS4, Policy CS5, Policy CS16 — source: `Southampton_Core_Strategy_2015_amended.pdf`

### Output (rag)

The Southampton Core Strategy (amended 2015) outlines a comprehensive spatial strategy and housing requirement aimed at creating an attractive, sustainable, and stimulating environment in the city. The key strategic policies relevant to this strategy include Policy CS4 (Housing Delivery), Policy CS5 (Housing Density), and Policy CS16 (Housing Mix and Type).

### Spatial Strategy

The spatial strategy emphasizes the need for effective housing delivery to meet the growing demand within Southampton. Policy CS4 highlights the importance of delivering a sufficient quantity of housing to support the city's population growth and economic development. It aims to ensure that housing developments are well-integrated into the urban fabric, contributing positively to the overall character and functionality of the city (Core Strategy, Page 36).

### Housing Requirement

1. **Housing Delivery (Policy CS4)**: This policy mandates that housing sites should be identified and developed to meet the city's housing needs. It emphasizes the need for a proactive approach to housing delivery, ensuring that developments are not only sufficient in number but also strategically located to enhance accessibility and sustainability (Core Strategy, Page 36).

2. **Housing Density (Policy CS5)**: This policy addresses the need for higher housing densities in certain areas to maximize land use efficiency while maintaining a balance with the quality of the living environment. It recognizes the pressure for increased densities to deliver necessary housing, particularly in urban areas where land is limited (Core Strategy, Page 38). The policy aims to ensure that developments are designed to create a unique sense of place while accommodating higher densities.

3. **Housing Mix and Type (Policy CS16)**: This policy focuses on the diversity of housing types and tenures to meet the varied needs of the community. It encourages a mix of affordable housing, family homes, and smaller units to cater to different demographics, including first-time buyers, families, and older residents. This approach is essential for creating inclusive communities and ensuring that housing provision reflects the needs of the population (Core Strategy, Page 54).

### Conclusion

In summary, the Southampton Core Strategy sets out a clear spatial strategy and housing requirement that prioritizes effective housing delivery, appropriate density, and a diverse housing mix. The strategic policies CS4, CS5, and CS16 collectively aim to create a sustainable urban environment that meets the needs of current and future residents while enhancing the overall quality of life in Southampton.

### Retrieved context (8 chunks — verify citations against these)

**[1] Southampton_Core_Strategy_2015_amended.pdf p.59 (city: southampton, score 0.8793)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  59 
5.2 Housing   
  
 
Policy CS 15 - Affordable Housing  
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S9 
S10 
S11 
 
On housing sites where 15 or more net dwellings are proposed, 

**[2] Southampton_Core_Strategy_2015_amended.pdf p.59 (city: southampton, score 0.8793)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  59 
5.2 Housing   
  
 
Policy CS 15 - Affordable Housing  
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S9 
S10 
S11 
 
On housing sites where 15 or more net dwellings are proposed, 

**[3] Southampton_Core_Strategy_2015_amended.pdf p.36 (city: southampton, score 0.8788)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  36 
centre.  Significant weight will not be placed on standard benefits from such 
developments (for example, general job creation). 
 
 
 
Policy CS 4 – Housing Delivery 
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
 
 
Link to Core Stra

**[4] Southampton_Core_Strategy_2015_amended.pdf p.36 (city: southampton, score 0.8788)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  36 
centre.  Significant weight will not be placed on standard benefits from such 
developments (for example, general job creation). 
 
 
 
Policy CS 4 – Housing Delivery 
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
 
 
Link to Core Stra

**[5] Southampton_Core_Strategy_2015_amended.pdf p.38 (city: southampton, score 0.8735)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  38 
 
Policy CS 5 – Housing Density 
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
SO6 – A unique sense of place 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S3 
S7 
S8 
S9 
S15 
 
Whilst there is continuing pressure for higher 

**[6] Southampton_Core_Strategy_2015_amended.pdf p.38 (city: southampton, score 0.8735)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  38 
 
Policy CS 5 – Housing Density 
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
SO6 – A unique sense of place 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S3 
S7 
S8 
S9 
S15 
 
Whilst there is continuing pressure for higher 

**[7] Southampton_Core_Strategy_2015_amended.pdf p.54 (city: southampton, score 0.871)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  54 
 
 
5 Key Requirements for Successful Development    
 
 
Policies in this Chapter: 
 
Design 
CS 13 Fundamentals of design   
CS 14 Historic environment   
 
Housing 
CS 15 Affordable housing   
CS 16  Housing mix and type   
CS 17 Gypsy & Traveller and travelling showpeople accommodation 
 
Transport a

**[8] Southampton_Core_Strategy_2015_amended.pdf p.54 (city: southampton, score 0.871)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  54 
 
 
5 Key Requirements for Successful Development    
 
 
Policies in this Chapter: 
 
Design 
CS 13 Fundamentals of design   
CS 14 Historic environment   
 
Housing 
CS 15 Affordable housing   
CS 16  Housing mix and type   
CS 17 Gypsy & Traveller and travelling showpeople accommodation 
 
Transport a

### Rubric (enter in the Evaluate page for `SOU-ES-01` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SOU-ST-02 — BASELINE

**City:** southampton | **Category:** strategic_analysis | **Difficulty:** medium

**Task:** What affordable housing percentage and site-size threshold applies to major residential developments in Southampton, and which local plan policy sets this? Answer for Southampton specifically.

**Expected policies (check these in the source PDF):** Policy CS15 — source: `Southampton_Core_Strategy_2015_amended.pdf`

### Output (baseline)

In Southampton, the provision of affordable housing for major residential developments is governed by the policies set out in the **Southampton City Council Local Plan**. Specifically, the relevant policy is **Policy CS15: Affordable Housing**, which is part of the Core Strategy adopted in 2015.

According to Policy CS15, the following key points apply:

1. **Affordable Housing Percentage**: The policy stipulates that major residential developments (defined as those comprising 10 or more dwellings) should provide a minimum of **30% affordable housing** on-site. This percentage is aimed at addressing the city's housing needs and ensuring a mix of housing types.

2. **Site-Size Threshold**: The threshold for major residential developments is set at **10 dwellings or more**. This means that any development proposal that includes 10 or more residential units will be required to meet the affordable housing provision as outlined in the policy.

3. **Types of Affordable Housing**: The policy also emphasizes the need for a mix of affordable housing types, including social rented, affordable rented, and intermediate housing, to cater to a diverse range of needs within the community.

4. **Viability Considerations**: It is important to note that the requirement for affordable housing may be subject to viability assessments. If a developer can demonstrate that the provision of 30% affordable housing would render the scheme unviable, the council may consider alternative arrangements, but this would need to be justified through a robust viability assessment.

In summary, for major residential developments in Southampton, the requirement is for **30% affordable housing** on sites of **10 or more dwellings**, as set out in **Policy CS15** of the Southampton City Council Local Plan. This policy is crucial for ensuring that the city meets its affordable housing needs and contributes to sustainable community development.

### Rubric (enter in the Evaluate page for `SOU-ST-02` / baseline)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |

---

## SOU-ST-02 — RAG

**City:** southampton | **Category:** strategic_analysis | **Difficulty:** medium

**Task:** What affordable housing percentage and site-size threshold applies to major residential developments in Southampton, and which local plan policy sets this? Answer for Southampton specifically.

**Expected policies (check these in the source PDF):** Policy CS15 — source: `Southampton_Core_Strategy_2015_amended.pdf`

### Output (rag)

In Southampton, the Core Strategy outlines the requirements for affordable housing in residential developments. Specifically, Policy CS 15 states that on housing sites where 15 or more net dwellings are proposed, or which exceed 0.5 hectares, a target of 35% affordable homes is required. This is applicable to larger sites (those with 15 or more units) (Extract 7).

For smaller sites, specifically those with between 5 to 14 units, the Core Strategy suggests a target of 20% affordable housing, as it has been determined that the higher percentage of 35% would be unviable for these smaller developments (Extract 3).

In summary, the affordable housing percentage and site-size thresholds for major residential developments in Southampton are as follows:
- **35% affordable housing** for sites of **15 or more net dwellings** or exceeding **0.5 hectares** (Policy CS 15).
- **20% affordable housing** for sites of **5 to 14 units** (Extract 3).

These provisions are set out in the Southampton Core Strategy, specifically under Policy CS 15.

### Retrieved context (8 chunks — verify citations against these)

**[1] Southampton_Core_Strategy_2015_amended.pdf p.90 (city: southampton, score 0.8028)**
> For residential development: The South East Plan sets a city wide requirement for 16,300 
dwellings in Southampton. Potential sites are identified by the Strategic Housing Land 
Availability Assessment (SHLAA). This demonstrates that the 16,300 dwelling target 
cannot be met solely on the lowest flood risk zone. Approximately 3,115 additional 
dwellings which do not currently have planning permiss

**[2] Southampton_Core_Strategy_2015_amended.pdf p.90 (city: southampton, score 0.8028)**
> For residential development: The South East Plan sets a city wide requirement for 16,300 
dwellings in Southampton. Potential sites are identified by the Strategic Housing Land 
Availability Assessment (SHLAA). This demonstrates that the 16,300 dwelling target 
cannot be met solely on the lowest flood risk zone. Approximately 3,115 additional 
dwellings which do not currently have planning permiss

**[3] Southampton_Core_Strategy_2015_amended.pdf p.60 (city: southampton, score 0.7849)**
> of 35% affordable homes on these larger sites.  The study also suggests that this 
level of provision on smaller sites would be unviable and suggests a target of 20% for 
sites of between 5 – 14 units.  
 
5.2.5 Within the overall provision for affordable housing the Southampton Housing Needs 
and Housing Market Survey, the South East Plan and the PUSH Affordable Housing 
Policy Framework indicate

**[4] Southampton_Core_Strategy_2015_amended.pdf p.60 (city: southampton, score 0.7849)**
> of 35% affordable homes on these larger sites.  The study also suggests that this 
level of provision on smaller sites would be unviable and suggests a target of 20% for 
sites of between 5 – 14 units.  
 
5.2.5 Within the overall provision for affordable housing the Southampton Housing Needs 
and Housing Market Survey, the South East Plan and the PUSH Affordable Housing 
Policy Framework indicate

**[5] Southampton_Core_Strategy_2015_amended.pdf p.60 (city: southampton, score 0.7758)**
> and intermediate affordable housing which is for households with incomes too low to 
buy or rent market housing but high enough to afford more than social housing rents. 
 
5.2.3 The South East Plan indicates that on average 30-40% of housing on new 
development sites in South Hampshire should be affordable.  The PUSH Affordable 
Housing Policy Framework suggests that up to 40% of affordable housi

**[6] Southampton_Core_Strategy_2015_amended.pdf p.60 (city: southampton, score 0.7757)**
> and intermediate affordable housing which is for households with incomes too low to 
buy or rent market housing but high enough to afford more than social housing rents. 
 
5.2.3 The South East Plan indicates that on average 30-40% of housing on new 
development sites in South Hampshire should be affordable.  The PUSH Affordable 
Housing Policy Framework suggests that up to 40% of affordable housi

**[7] Southampton_Core_Strategy_2015_amended.pdf p.59 (city: southampton, score 0.7667)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  59 
5.2 Housing   
  
 
Policy CS 15 - Affordable Housing  
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S9 
S10 
S11 
 
On housing sites where 15 or more net dwellings are proposed, 

**[8] Southampton_Core_Strategy_2015_amended.pdf p.59 (city: southampton, score 0.7667)**
> Southampton City Council, Core Strategy – Amended Adopted Version March 2015 January 2010  59 
5.2 Housing   
  
 
Policy CS 15 - Affordable Housing  
 
Link to City of Southampton Strategy objective(s): 
SO4 – An attractive, sustainable and stimulating environment 
  
 
Link to Core Strategy 
Strategic objective(s): 
 
S9 
S10 
S11 
 
On housing sites where 15 or more net dwellings are proposed, 

### Rubric (enter in the Evaluate page for `SOU-ST-02` / rag)

| Metric | Scale | Score |
|---|---|---|
| Accuracy | 1-5 |  |
| Completeness | 1-5 |  |
| Planning usefulness | 1-5 |  |
| Grounding | 0-2 |  |
| Hallucination present? | y/n |  |
| Hallucination type | fabricated_clause / outdated_policy / spatial_misattribution / confident_ambiguity / none |  |
