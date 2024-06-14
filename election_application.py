""" Counts the number of votes and seats for the Netherlands for each party. 
There are further expanions possible like adding other countries, party information, converting the seats into EU fractions, graphics (visualizations but it is not possible in this environment) and persons.
Hours spent until now: 11
to do: 
Add information on every party 
See if I can upload the project with git 
 """



SEATS_NL = 31
POLITICAL_PARTIES = ["Groenlinks/PvdA", "VVD", "CDA", "FvD", "D66", "PvdD", "50Plus", "PVV", "Ja21", "CU", "SGP", "BBB", "MDD", "SP", "Vanderegio", "Volt", "BvNL", "NSC", "PP/de Groenen"]

def main():
    # intro message
    print("Election Application")
    print("")
    menu_choice = int(input("This is an application with which the votes of the European Election for the parties of the Netherlands can be counted. It can also show you information on each of the parties. Press 1 for the vote counter or 2 for information. "))
    
    if menu_choice == 1:
        # message that explains the voting
        print("")
        print("Enter the counted votes for each party. The Netherlands will be having 31 members in the European Parliament. In total the European Parliament has a maximum of 751 seats. ")
        print("")

        # counts the votes and seats for the nl and prints them 
        # counts the votes for every party
        # makes a dictionary of all the votes and gives the total of votes
        dict_votes = count_votes()
        total_votes = sum(dict_votes.values())
        print("")
        print("The total of votes is " + str(total_votes))

        # calculates the voting quota which is the amount of votes divided by the number of seats 
        vote_quota = float(total_votes / SEATS_NL)
        print("The vote quota is " + str(vote_quota))

        # calculates and print the seats 
        print("")
        dict_seats = {}
        for key, value in dict_votes.items():
            print("The number of whole seats for " + key + " is " + str(int(value / vote_quota)))
        print("")
        for key, value in dict_votes.items():
            print("The residual of seats for " + key + " is " + str(value % vote_quota))
        for key, value in dict_votes.items():
            dict_seats[key] = int(value / vote_quota)
        print("")
        print("This is the total of seats for each party before dividing the residual of seats: "+ str(dict_seats))

        # residual seats 
        # calculates the total of seats until now 
        total_seats = sum(dict_seats.values())
        print("")
        print("The total of seats taken until now is " + str(total_seats) + ". That means there are " + str(SEATS_NL - total_seats) + " left to be divided.")
        # first residual seat (method of biggest mean). A party can get a residual seat if it has at least 1 seat.
        # the votes are divided by the amount of seats +1. The party with the highest resulting mean gets the first residual seat.
        # the mean gets recalculated after every assignment of a residual seat

        # calculates the means
        means_dict = {}
        for key, value in dict_seats.items():
            if dict_seats[key] >= 1:
               means_dict[key] = dict_votes[key] / (dict_seats[key] + 1)
            else:
                means_dict[key] = 0
        print("")
        print("These are the means that are calculated according to the highest average mean method that is used in calculating the residual seats: " + str(means_dict))


        # assigns the residual seats
        print("")
        while total_seats < 31:
            max_mean = max(means_dict, key = lambda x: means_dict[x])
            print("A residual seat goes to: " + str(max_mean))
            print("")
            # del means_dict[max(means_dict, key=means_dict.get)]
            total_seats = total_seats + 1
            # add the residual to the total of seats 
            dict_seats[max_mean] += 1
            # recalculate the mean
            means_dict[max_mean] = dict_votes[max_mean] / (dict_seats[max_mean] + 1)
            print("The new means are: " + str(means_dict))
            print("")
        print("")
        print("The total of seats for each party is now: " + str(dict_seats))
        
    # program goes to option 2: information on the parties
    if menu_choice == 2:
        information_tool()



    # optional: other countries
    # optional: converting the seats to fractions
    # optional: graphics
    # optional: persons

def count_votes():
    # tool that lets the user count the votes for every party
    vote_count = {}
    for party_name in POLITICAL_PARTIES:
        vote_count[party_name] = int(input("How many votes are there for " + party_name + "? "))
    print("")
    print("These are the votes for every party: " + str(vote_count))
    return vote_count

def information_tool():
    # gives information on all the participating parties. Possibly has other user rights than menu option 1. This can be for all inhabitants. 
    print("")
    party_input = input("These are the participating political parties: " + str(POLITICAL_PARTIES) + ". On which party do you want some information? There is information available on Groenlinks/PvdA, VVD, PvdD, 50Plus and Vanderegio. Type references if you want to see the references. ")
    if party_input.lower() == ("groenlinks/pvda"):
        print("")
        print("Groenlinks/PvdA is a fusion party of Groenlinks and PvdA. They came together in 2023. Bas Eickhout is the leader for the European Elections. ")
        print("")
        print("For the European Elections 2024 they have formulated 10 concrete plans. These plans are: ")
        print("1: Raising the minimum wage to the same amount in the whole European Union. ")
        print("2: The European Union is climate neutral in 2040. Therefore there will be binding commitments about fossil fuels. There will be more subsidies for fossil fuels. ")
        print("3: More money should go to social rent. There has to come an European crisis plan for housing. They have to be livable, sustainable and payable for everyone. ")
        print("4: European right on abortion. ")
        print("5: LHBTQUIA+'s should be able to be themselves. There should be no laws against them. ")
        print("6: Investments in train travel. It has to be quick, with a large network and payable as a sustainable alternative for airplanes. There should come one booking system for the whole European Union. They will help people with isolating their houses. ")
        print("7: Clean energy for everyone like sun, water and wind energy. They will work for a supernet which combines electricity networks. ")
        print("8: Tackle tax evasion: mainly by large companies. ")
        print("9: The Erasmus program for student exchange should be available for more. ")
        print("10: One European museum card. ")
        print("Other important points in the program are livelihood security, rights, equality (for example in marrying who you want) and democracy, green agriculture with fair prices, safe internet, trusting Europe, strong and green European companies, safe and equal migration, a cease fire between Palestine and Israel and supporting Ukraine.")
        information_tool()
    elif party_input.lower() == ("vvd"):
        print("")
        print("The VVD was founded in 1948. ")
        print("")
        print("Malik Azmani is the party leader for the European Elections. The main focus areas the VVD has for the European Elections are the EU and the world, outside borders, the economy, the modern human, finance and institutions. ")
        information_tool()
    elif party_input.lower() == ("pvdd"):
        print("")
        print("The Partij voor de Dieren was formed in 2002. It was the first party in the world that defended the interest of non-humans. The interests of animals were central to their party program. In their eyes this topic was not high enough on the agenda. In 2006 the party came into the House of Representatives with two seats. Since 2012 the party is active on world-level with the Animal Politics Foundation. The party was founded by Marianne Thieme and Lieke Keller. ")
        print("")
        print("Main points in the European Elections are respect for animals, more nature, a food revolution, climate action, a healthy living environment and a different economy. They want to close down the cattle industry, end very large animal transports, free animals in the animal industry from their cages, stop illegal trade in puppy's and the murder of stray dogs and cats in Europe and to have camera surveillance in slaughter houses. They also want to end slaughter without anesthesia. They want nature to be respected and protected and to end the hunt. They want to save the seas and oceans against pollution and over-fishery. They want to end the use of pesticides in agriculture. They want to end EU subsidies on the cattle industry, destructive agriculture and bull fighting. Money should go to farmers that focus on healthy, sustainable and plant-based food production. The import on harmful products should be stopped. The EU has to be climate neutral by 2040, fossile subsidies should end and private yets and super yachts should be forbidden. The air and water should be clean and the soil healthy. The requirements for harmful industry emissions should be stricter. PFAS and other every harmful substances should be forbidden. The economy has to take the earth into account. Victims of war and violence should be cared for. Fundamental rights and democracy are important. You should be able to be yourself. The big polluters have to be stopped. ")
        print("")
        print("Anja Hazekamp is the leader of the list in the European Elections. Esther Ouwehand is the leader of the party. ")
        information_tool()
    elif party_input.lower() == ("50plus"):
        print("")
        print("50Plus was founded in 2009 by Jan Nagel, Ton Luiting, Alexander Müninghoff, Maurice Koopman & Kees de Lange. It has as a goal to stick up for the interests of people above 50. Jan Nagel was a member of PvdA, one of the founders of Leefbaar Nederland and one of the founders of PRDV before this. The name 50Plus has been used since 2011. As main points in the program they started with lowering the pension age to 65, higher purchasing power for the elderly and better and cheaper healthcare. They also wanted reforms like referenda and the abolishment of the Senate. They wanted a strict but righteous immigration asylum policy and were progressive in the fields of the environment, euthanasia and soft drugs. In most two-dimensional models they are seen as a center party with a light tendency to the progressive and left.")
        print("")
        print("Now with the European Elections 50Plus wants to strengthen the position of people above 50 in the European Union. They want an influential European Commissioner because of policies about the ageing population. This is called vergrijzing in Dutch: people becoming more gray because they are older on average. They also want more money for the fabrication of medicine in Europe. Also cities have to become more age-friendly. They want stricter controls on outside borders to lessen migration. Refugees have to be taken care of in the region itself. They have to know within one year if they can stay. They have to be divided evenly across the different members. They find it also important to solve inequality in game rules between member states. What countries can do themselves the European Union should not get involved with. There should be more collaboration in the field of security in the creation of an European army. There should also be more collaboration in the BeNeLux and in the field of sustainability. There should be more support for small-scale organic agriculture instead of intensive large-scale agriculture. They also think there should be more money for research and innovation. There also should be more transparancy and influence in European decision-making. Also there should be more controls on the enforcement of rules. They think the location of meetings should be changed from Straatsburg to somewhere else. ")
        print("")
        print("Martin van Rooijen is the leader of the party. Adriana A. Hernández Martínez is the leader of the European Elections list. ")
        information_tool()
    elif party_input.lower() == ("vanderegio"):
        print("")
        print("Vanderegio is a party that started as a electoral association in 2019 to get more attention for local interests. They formed a list with the Piratenpartij in 2019. The party leader is Sent Wierda. ")
        print("")
        print("Vanderegio work a lot with theses in their party program. Countries that do have media freedom have to be punished financially. The EU has to able to intervene when fundamental European values are violated by European countries in their policies. Every country has to have veto right. Only members states can tax, not the EU itself. Ex-members of the European Parliament are not allowed to lobby for a period of 2,5 years. Up to 10 years is also ok. The EU gives less money to members that do not respect European values about democracy. The European Parliament has to have the right to send away the European Commissioner. The European Parliament should be able to make law proposals. It should be possible to send away a member that does not abide to fundamental democratic principles. A bigger budget deficit should be allowed for member countries. The Union should watch budget deficits more strict and closely.")
        print("Nuclear energy is not sustainable. They want more European Parliament and less Council of Europe. They want open sollicitations for European Commissioners. There should not be an European army. The European Union has to confirm Palestine as a state. Dutch people that went to Syria to fight are not allowed to return in freedom. War crimes have to be punished. Defense of a country can be done in many ways before a military operation is necessary. The deliverance of weapons to Ukraine is counter-productive: Russia should be held for the Internatial Court of Justice. The European Union should be independent in the conflict between Israel and Palestine.")
        print("The minimum age to vote should be 16. Referenda should be possible in countries at the same time. The head of the European Commission should be chosen directly. Taxes on flights have to make travel by train the better option. There should not come more border controls. Fingerprints in passports are not a good idea. More money should go to train developments. It should become more expensive to import electric cars out of China than those of the European Union. Asylum seekers have to be divided over the member states evenly. All countries need to have to same rules about asylum seekers who want to be together with their family. There should not come a maximum on asylum seekers. Public goods like roads and electricity should be public. Internships should be paid. Vanderegio wants the Netherlands to be in the European Union but a referendum should be possible. Countries can only be a part of the EU when they meet all conditions without exceptions. New members are possible. Strong members should support weaker members. Countries have to able to make own rules on certain topics. Diversity of members states has to respected. Policy making should be as close to the inhabitants as possible. Integration of migrants is important. Inhabitants have to able to move freely in the European Union and it should be more easy for schooled workers to work here. Members should be able to block takeovers of companies.")
        print("The Union has to make stronger enviromental rules for products outside of the Union. The export of trash has to be forbidden. EU goals for CO2 reductions have to be followed stricter. Energy has to become more sustainable. The whole world has to work together against climate change. Companies have to pay more with more C02 emissions. There should be a natural gas reserve for all members together. There has to be more cooperation against online crime. Social media companies can make their own policies on fake news. GMOs should not be allowed. Animal transports should not take longer than 4 hours. The EU should stop with subsidies to the intensive cattle industry. The Netherlands should be able to have more nitrogen emissions because of it's high population density. Glyphosate has to be forbidden.")
        print("Every member has to have a minimum wage. Social security is important. There should come alternatives for animal testing. There should come a digital euro. Big companies have to pay a minimum tax. EU members have to be able to decide themselves how much they tax company profit. Members should buy medicine together and put money in making medicine in Europe. Taxes on tobacco should be the same across member states. The European Union should cheer countries on in supporting same sex marriage.")      
        information_tool()
    elif party_input.lower() == ("references"):
        print("")
        print("Wielenga, F. van Baalen, C. & Wilp, M. (2018). Een versplinterd landschap. Bijdragen over geschiedenis en actualiteit van Nederlandse politieke partijen. Amsterdam University Press. ")
        print("https://www.vvd.nl/onze-geschiedenis/")
        print("https://www.partijvoordedieren.nl/organisatie")
        print("https://www.partijvoordedieren.nl/europese-verkiezingen")  
        print("https://www.rug.nl/research/dnpp/politieke-partijen/50plus/geschiedenis/")
        print("https://50pluspartij.nl/verkiezingsprogramma-voor-het-europees-parlement-2024-2029/#euro")
        print("https://50pluspartij.nl/mensen/")
        print("https://vanderegio.nl/thema/")
        print("https://groenlinkspvda.nl/wp-content/uploads/2024/05/vkep2024definitiefhelderetaal.pdf")
        print("https://groenlinkspvda.nl/verkiezingsprogramma-europa/")
        print("https://groenlinkspvda.nl/blog/10-plannen-groenlinks-pvda-in-europa/")
        print("https://groenlinkspvda.nl/onze-mensen-voor/kandidaten-europees-parlement/")
        print("")
        information_tool()
    
    


    
    
    


    

    

    

if __name__ == "__main__":
    main()