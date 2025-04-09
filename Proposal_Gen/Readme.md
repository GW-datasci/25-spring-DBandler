Capstone Project Proposal
Name: Daniel Bandler
Objective


Nationwide, over 40% of Americans are obese, and 20% of American youths suffer from this condition, leading to severe health complications such as diabetes, heart disease, and dental decay. Policymakers have proposed soda taxes as a way to curb sugar consumption and reduce obesity-related diseases. These taxes function as Pigouvian incentives, raising the price of sugary beverages and encouraging consumers to substitute with healthier alternatives. While international case studies suggest soda taxes can decrease consumption, their impact on long-term health metrics such as obesity and diabetes remains uncertain (Itria et al., 2021). This project seeks to evaluate whether U.S. soda taxes have led to public health improvements.

Impact:
This project will have clear public health implications. Sugar taxes continue to be floated by policymakers, and criticised by beverage vendors, as obesity continues to rise. The topic of this study will continue to be relevant to public health policymakers in the years to come.

My ultimate datasource is the CDC, which is the gold-standard for national data of this type.
Data comes from here: https://www.ruralhealthinfo.org/data-explorer?id=196 (Originally, CDC). County level obesity data.

County Level Diabetes: https://gis.cdc.gov/grasp/diabetes/diabetesatlas-surveillance.html# 

Self-reported Behavioral Risk Survey. Has questions about diabetes, physical conditioning, dental decay, healthy food consumption, etc:
https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/j32a-sa6u/about_data
I have data for each county in the United States over time.

Approach
[Talk about how you plan on approaching this capstone through several steps. List the steps
Below.]


No US states have instituted a sugar tax, but several cities have, including DC, Seattle, Boulder, San Francisco, and Philadelphia. While I do not have city level data, I do have county level data, and DC, Philadelphia and San Francisco are coterminous with their counties. 


I will select 1 location(or possibly multiple if the policy dates align) and compare them to a synthetic control constructed from a basket of urban counties lacking a sugar tax, such as New York County, Fulton County (Atlanta), LA County, City of Baltimore, Denver, and more. I am most interested in Philadelphia, as their 2017 tax was set relatively high at 1.5c/oz, a price that adds over a dollar to a two liter bottle.

If I use the behavioral survey, I can do that on the metropolitan level, but that will take some time geolocating and selecting the cities I want through ArcGIS Pro.

I am late to the game here, so my timeline will have to be abbreviated. This is a rough timeline for this project:
Steps:
Data Preparation & Exploration:
Identify counties corresponding to cities with soda taxes. Generate explanatory data.
Select a control group of comparable urban counties without a soda tax
Synthetic Control Construction:
Construct a synthetic control group out of the relative indicator levels for control cities.
Causal Inference & Model Evaluation:
Compare post-tax trends in treated vs. synthetic control counties.
Conduct robustness tests, analysis
Write-up:
Interpret findings, conduct a thorough literature review, provide data and explanatory data.


Possible Issues
Unlike my last topic idea (healthcare in VT) I have the data, I know I can use the data, and I know how I can use the data. Everything here is publicly available, which reduced many of my hurdles.
Lack of effect. Either the tax is too small, too long run, or for whatever reason, soda is resistant to the Pigouvian effect.
Substitution, spillovers. A tax on sugary drinks may have lead to an increase in consumption of other sweet foods, as occurred in Philadelphia. (Lozano-Rojas and Carlin, 2021). This tax also fails to capture purchases that occur out of city lines.

Itria A, Borges SS, Rinaldi AEM, Nucci LB, Enes CC. Taxing sugar-sweetened beverages as a policy to reduce overweight and obesity in countries of different income classifications: a systematic review. Public Health Nutr. 2021 Nov;24(16):5550-5560. doi: 10.1017/S1368980021002901. Epub 2021 Jul 5. PMID: 34218837; PMCID: PMC10195460.

Klonoff DC. A sweetened beverage tax is needed to combat the obesity epidemicas well as related absenteeism and presenteeism. J Diabetes Sci Technol. 2009 May 1;3(3):408-10. doi: 10.1177/193229680900300301. PMID: 20144275; PMCID: PMC2769883.

Lozano-Rojas F, Carlin P. The effect of soda taxes beyond beverages in Philadelphia. Health Econ. 2022 Nov;31(11):2381-2410. doi: 10.1002/hec.4586. Epub 2022 Aug 17. PMID: 35978481; PMCID: PMC9804786.
