using System;
using System.Collections.Generic;
[System.Serializable]
public class Law : BaseElement
{
    // Code
    public string Decree;
    public int? Date;
    public string Purpose;
    public string AuthorId;
    // Compulsion
    public List<string> JurisdictionsIds; = new List<string>();
    public List<string> ProhibitionsIds; = new List<string>();
    public List<string> PenaltiesIds; = new List<string>();
    public List<string> AdjudicatorsIds; = new List<string>();
    public List<string> EnforcersIds; = new List<string>();
}
