using System;
using System.Collections.Generic;
[System.Serializable]
public class Family : BaseElement
{
    // Identity
    public string Spirit;
    public string History;
    public List<string> TraditionsIds; = new List<string>();
    public List<string> TraitsIds; = new List<string>();
    public List<string> AbilitiesIds; = new List<string>();
    public List<string> LanguagesIds; = new List<string>();
    public List<string> AncestorsIds; = new List<string>();
    // World
    public string Reputation;
    public List<string> EstatesIds; = new List<string>();
    public List<string> GovernsIds; = new List<string>();
    public List<string> HeirloomsIds; = new List<string>();
    public List<string> CreaturesIds; = new List<string>();
}
