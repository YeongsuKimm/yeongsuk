---
toc: True
comments: False
layout: default
title: JS output Table
description: San Diego Padres stats table
type: tangibles
courses: {'compsci': {'week': 2}}
---

<html>
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>    
</head>
<body>
    <h3>Markdown has an easier and more comprehendible syntax compared to html.</h3>
    <h3>HTML decides the content that the page will contain as JavaScript determines the functionality behind each feature.</h3>
    <h3>Using JavaScript along with a table is useful when trying to search through a lot of list items as it can help to search or sort them in a specific way.</h3>
    <table id="demo" class="table cell-border">
        <thead>
            <tr>
                <td>Year</td>
                <td>Total W-L</td>
                <td>World Series Winner</td>
                <td>Win Percentage</td>
                <td>Position (NL West)</td>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>2022</td>
                <td>89-73</td>
                <td>Houston Astros</td>
                <td>.549</td>
                <td>2</td>
            </tr>
            <tr>
                <td>2021</td>
                <td>79-83</td>
                <td>Atlanta Braves</td>
                <td>.488</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2020</td>
                <td>37-23</td>
                <td>Los Angeles Dodgers</td>
                <td>.617</td>
                <td>2</td>
            </tr>
            <tr>
                <td>2019</td>
                <td>70-92</td>
                <td>Washington Nationals</td>
                <td>.432</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2018</td>
                <td>66-96</td>
                <td>Boston Red Sox</td>
                <td>.407</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2017</td>
                <td>71-91</td>
                <td>Houston Astros</td>
                <td>.438</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2016</td>
                <td>68-94</td>
                <td>Chicago Cubs</td>
                <td>.420</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2015</td>
                <td>74-88</td>
                <td>Kansas City Royals</td>
                <td>.457</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2014</td>
                <td>77-85</td>
                <td>San Francisco Giants</td>
                <td>.475</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2013</td>
                <td>76-86</td>
                <td>Boston Red Sox</td>
                <td>.469</td>
                <td>T3</td>
            </tr>
            <tr>
                <td>2012</td>
                <td>76-86</td>
                <td>San Francisco Giants</td>
                <td>.469</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2011</td>
                <td>71-91</td>
                <td>St. Louis Cardinals</td>
                <td>.438</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2010</td>
                <td>90-72</td>
                <td>San Francisco Giants</td>
                <td>.556</td>
                <td>2</td>
            </tr>
            <tr>
                <td>2009</td>
                <td>75-87</td>
                <td>New York Yankees</td>
                <td>.463</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2008</td>
                <td>63-99</td>
                <td>Philadelphia Phillies</td>
                <td>.389</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2007</td>
                <td>89-74</td>
                <td>Boston Red Sox</td>
                <td>.546</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2006</td>
                <td>88-74</td>
                <td>St. Louis Cardinals</td>
                <td>.543</td>
                <td>T1</td>
            </tr>
            <tr>
                <td>2005</td>
                <td>82-80</td>
                <td>Chicago White Sox</td>
                <td>.506</td>
                <td>1</td>
            </tr>
            <tr>
                <td>2004</td>
                <td>87-75</td>
                <td>Boston Red Sox</td>
                <td>.537</td>
                <td>3</td>
            </tr>
            <tr>
                <td>2003</td>
                <td>64-98</td>
                <td>Florida Marlins</td>
                <td>.395</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2002</td>
                <td>66-96</td>
                <td>Anaheim Angels</td>
                <td>.407</td>
                <td>5</td>
            </tr>
            <tr>
                <td>2001</td>
                <td>79-83</td>
                <td>Arizona Diamondbacks</td>
                <td>.488</td>
                <td>4</td>
            </tr>
            <tr>
                <td>2000</td>
                <td>76-86</td>
                <td>New York Yankees</td>
                <td>.469</td>
                <td>5</td>
            </tr>
        </tbody>
    </table>
</body>
<script>
    $("#demo").DataTable();
</script>
</html>