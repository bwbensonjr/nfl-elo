---
execute:
  echo: false
title: NFL Elo
toc-title: Table of contents
---

## NFL Elo

:::: {.cell execution_count="1"}
::: {.cell-output .cell-output-display execution_count="1"}
<div id="kzmqzyuwft" style="padding-left:0px;padding-right:0px;padding-top:10px;padding-bottom:10px;overflow-x:auto;overflow-y:auto;width:auto;height:auto;">
<style>
#kzmqzyuwft table {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', 'Fira Sans', 'Droid Sans', Arial, sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
        }

#kzmqzyuwft thead, tbody, tfoot, tr, td, th { border-style: none; }
 tr { background-color: transparent; }
#kzmqzyuwft p { margin: 0; padding: 0; }
 #kzmqzyuwft .gt_table { display: table; border-collapse: collapse; line-height: normal; margin-left: auto; margin-right: auto; color: #333333; font-size: 16px; font-weight: normal; font-style: normal; background-color: #FFFFFF; width: auto; border-top-style: solid; border-top-width: 2px; border-top-color: #A8A8A8; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #A8A8A8; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; }
 #kzmqzyuwft .gt_caption { padding-top: 4px; padding-bottom: 4px; }
 #kzmqzyuwft .gt_title { color: #333333; font-size: 125%; font-weight: initial; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; border-bottom-color: #FFFFFF; border-bottom-width: 0; }
 #kzmqzyuwft .gt_subtitle { color: #333333; font-size: 85%; font-weight: initial; padding-top: 3px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; border-top-color: #FFFFFF; border-top-width: 0; }
 #kzmqzyuwft .gt_heading { background-color: #FFFFFF; text-align: center; border-bottom-color: #FFFFFF; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kzmqzyuwft .gt_bottom_border { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kzmqzyuwft .gt_col_headings { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; }
 #kzmqzyuwft .gt_col_heading { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; overflow-x: hidden; }
 #kzmqzyuwft .gt_column_spanner_outer { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: normal; text-transform: inherit; padding-top: 0; padding-bottom: 0; padding-left: 4px; padding-right: 4px; }
 #kzmqzyuwft .gt_column_spanner_outer:first-child { padding-left: 0; }
 #kzmqzyuwft .gt_column_spanner_outer:last-child { padding-right: 0; }
 #kzmqzyuwft .gt_column_spanner { border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: bottom; padding-top: 5px; padding-bottom: 5px; overflow-x: hidden; display: inline-block; width: 100%; }
 #kzmqzyuwft .gt_spanner_row { border-bottom-style: hidden; }
 #kzmqzyuwft .gt_group_heading { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; text-align: left; }
 #kzmqzyuwft .gt_empty_group_heading { padding: 0.5px; color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; vertical-align: middle; }
 #kzmqzyuwft .gt_from_md> :first-child { margin-top: 0; }
 #kzmqzyuwft .gt_from_md> :last-child { margin-bottom: 0; }
 #kzmqzyuwft .gt_row { padding-top: 8px; padding-bottom: 8px; padding-left: 5px; padding-right: 5px; margin: 10px; border-top-style: solid; border-top-width: 1px; border-top-color: #D3D3D3; border-left-style: none; border-left-width: 1px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 1px; border-right-color: #D3D3D3; vertical-align: middle; overflow-x: hidden; }
 #kzmqzyuwft .gt_stub { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; }
 #kzmqzyuwft .gt_stub_row_group { color: #333333; background-color: #FFFFFF; font-size: 100%; font-weight: initial; text-transform: inherit; border-right-style: solid; border-right-width: 2px; border-right-color: #D3D3D3; padding-left: 5px; padding-right: 5px; vertical-align: top; }
 #kzmqzyuwft .gt_row_group_first td { border-top-width: 2px; }
 #kzmqzyuwft .gt_row_group_first th { border-top-width: 2px; }
 #kzmqzyuwft .gt_table_body { border-top-style: solid; border-top-width: 2px; border-top-color: #D3D3D3; border-bottom-style: solid; border-bottom-width: 2px; border-bottom-color: #D3D3D3; }
 #kzmqzyuwft .gt_sourcenotes { color: #333333; background-color: #FFFFFF; border-bottom-style: none; border-bottom-width: 2px; border-bottom-color: #D3D3D3; border-left-style: none; border-left-width: 2px; border-left-color: #D3D3D3; border-right-style: none; border-right-width: 2px; border-right-color: #D3D3D3; }
 #kzmqzyuwft .gt_sourcenote { font-size: 90%; padding-top: 4px; padding-bottom: 4px; padding-left: 5px; padding-right: 5px; text-align: left; }
 #kzmqzyuwft .gt_left { text-align: left; }
 #kzmqzyuwft .gt_center { text-align: center; }
 #kzmqzyuwft .gt_right { text-align: right; font-variant-numeric: tabular-nums; }
 #kzmqzyuwft .gt_font_normal { font-weight: normal; }
 #kzmqzyuwft .gt_font_bold { font-weight: bold; }
 #kzmqzyuwft .gt_font_italic { font-style: italic; }
 #kzmqzyuwft .gt_super { font-size: 65%; }
 #kzmqzyuwft .gt_footnote_marks { font-size: 75%; vertical-align: 0.4em; position: initial; }
 #kzmqzyuwft .gt_asterisk { font-size: 100%; vertical-align: 0; }
 
</style>

  week   away_team   away_elo   away_win_prob   away_score   home_team   home_elo   home_win_prob   home_score   point_spread   actual_spread
  ------ ----------- ---------- --------------- ------------ ----------- ---------- --------------- ------------ -------------- ---------------
  1      BAL         1,638      41%             20           KC          1,649      59%             27           −2             −7
  1      GB          1,562      48%             29           PHI         1,528      52%             34           −1             −5
  1      PIT         1,534      57%             18           ATL         1,435      43%             10           2              8
  1      ARI         1,410      18%             28           BUF         1,628      82%             34           −11            −6
  1      TEN         1,436      39%             17           CHI         1,465      61%             24           −3             −7
  1      NE          1,408      24%             16           CIN         1,559      76%             10           −8             6
  1      HOU         1,498      47%             29           IND         1,467      53%             27           −1             2
  1      JAX         1,489      35%             17           MIA         1,543      65%             20           −4             −3
  1      CAR         1,349      22%             10           NO          1,521      78%             47           −9             −37
  1      MIN         1,489      47%             28           NYG         1,458      53%             6            −1             22
  1      LV          1,501      51%             10           LAC         1,444      49%             22           0              −12
  1      DEN         1,470      38%             20           SEA         1,503      62%             26           −3             −6
  1      DAL         1,583      54%             33           CLE         1,502      46%             17           1              16
  1      WAS         1,385      25%             20           TB          1,527      75%             37           −8             −17
  1      LA          1,523      36%             20           DET         1,574      64%             26           −4             −6
  1      NYJ         1,452      19%             19           SF          1,651      81%             32           −10            −13
  2      BUF         1,635      55%             31           MIA         1,552      45%             10           1              21
  2      LV          1,475      24%             26           BAL         1,621      76%             23           −8             3
  2      LAC         1,471      62%             26           CAR         1,333      38%             3            3              23
  2      NO          1,537      33%             44           DAL         1,609      67%             19           −5             25
  2      TB          1,542      36%             20           DET         1,588      64%             16           −4             4
  2      IND         1,456      31%             10           GB          1,545      69%             16           −6             −6
  2      CLE         1,476      42%             18           JAX         1,479      58%             13           −2             5
  2      SF          1,661      62%             17           MIN         1,522      38%             23           4              −6
  2      SEA         1,518      54%             23           NE          1,438      46%             20           1              3
  2      NYJ         1,442      46%             24           TEN         1,420      54%             17           −1             7
  2      NYG         1,425      51%             18           WAS         1,370      49%             21           0              −3
  2      LA          1,509      58%             10           ARI         1,403      42%             41           2              −31
  2      PIT         1,553      57%             13           DEN         1,456      43%             6            2              7
  2      CIN         1,529      25%             25           KC          1,666      75%             26           −7             −1
  2      CHI         1,481      39%             13           HOU         1,509      61%             19           −3             −6
  2      ATL         1,416      26%             22           PHI         1,545      74%             21           −7             1
  3      NE          1,425      37%             3            NYJ         1,464      63%             24           −4             −21
  3      NYG         1,411      31%             None         CLE         1,497      69%             None         −5             None
  3      CHI         1,466      46%             None         IND         1,444      54%             None         −1             None
  3      HOU         1,524      40%             None         MIN         1,547      60%             None         −3             None
  3      PHI         1,535      37%             None         NO          1,580      63%             None         −4             None
  3      LAC         1,494      33%             None         PIT         1,571      67%             None         −5             None
  3      DEN         1,438      27%             None         TB          1,562      73%             None         −7             None
  3      GB          1,557      65%             None         TEN         1,397      35%             None         4              None
  3      CAR         1,309      20%             None         LV          1,496      80%             None         −9             None
  3      MIA         1,524      42%             None         SEA         1,531      58%             None         −2             None
  3      DET         1,568      61%             None         ARI         1,444      39%             None         3              None
  3      BAL         1,600      48%             None         DAL         1,565      52%             None         −1             None
  3      SF          1,637      66%             None         LA          1,469      34%             None         5              None
  3      KC          1,670      75%             None         ATL         1,426      25%             None         8              None
  3      JAX         1,458      19%             None         BUF         1,663      81%             None         −10            None
  3      WAS         1,384      25%             None         CIN         1,526      75%             None         −8             None
  4      DAL         1,565      65%             None         NYG         1,411      35%             None         4              None
  4      NO          1,580      65%             None         ATL         1,426      35%             None         4              None
  4      CIN         1,526      72%             None         CAR         1,309      28%             None         7              None
  4      LA          1,469      43%             None         CHI         1,466      57%             None         −2             None
  4      MIN         1,547      41%             None         GB          1,557      59%             None         −2             None
  4      JAX         1,458      34%             None         HOU         1,524      66%             None         −5             None
  4      PIT         1,571      61%             None         IND         1,444      39%             None         3              None
  4      DEN         1,438      36%             None         NYJ         1,487      64%             None         −4             None
  4      PHI         1,535      39%             None         TB          1,562      61%             None         −3             None
  4      WAS         1,384      35%             None         ARI         1,444      65%             None         −4             None
  4      NE          1,402      16%             None         SF          1,637      84%             None         −11            None
  4      KC          1,670      67%             None         LAC         1,494      33%             None         5              None
  4      CLE         1,497      43%             None         LV          1,496      57%             None         −2             None
  4      BUF         1,663      52%             None         BAL         1,600      48%             None         1              None
  4      TEN         1,397      26%             None         MIA         1,524      74%             None         −7             None
  4      SEA         1,531      38%             None         DET         1,568      62%             None         −3             None
  5      TB          1,562      62%             None         ATL         1,426      38%             None         3              None
  5      NYJ         1,487      35%             None         MIN         1,547      65%             None         −4             None
  5      CAR         1,309      23%             None         CHI         1,466      77%             None         −8             None
  5      BAL         1,600      53%             None         CIN         1,526      47%             None         1              None
  5      BUF         1,663      63%             None         HOU         1,524      37%             None         4              None
  5      IND         1,444      41%             None         JAX         1,458      59%             None         −3             None
  5      MIA         1,524      60%             None         NE          1,402      40%             None         3              None
  5      CLE         1,497      59%             None         WAS         1,384      41%             None         2              None
  5      LV          1,496      51%             None         DEN         1,438      49%             None         0              None
  5      ARI         1,444      20%             None         SF          1,637      80%             None         −10            None
  5      GB          1,557      56%             None         LA          1,469      44%             None         2              None
  5      NYG         1,411      27%             None         SEA         1,531      73%             None         −7             None
  5      DAL         1,565      42%             None         PIT         1,571      58%             None         −2             None
  5      NO          1,580      31%             None         KC          1,670      69%             None         −6             None
  6      SF          1,637      58%             None         SEA         1,531      42%             None         2              None
  6      JAX         1,458      42%             None         CHI         1,466      58%             None         −2             None
  6      WAS         1,384      18%             None         BAL         1,600      82%             None         −11            None
  6      ARI         1,444      28%             None         GB          1,557      72%             None         −7             None
  6      HOU         1,524      60%             None         NE          1,402      40%             None         3              None
  6      TB          1,562      40%             None         NO          1,580      60%             None         −3             None
  6      CLE         1,497      38%             None         PHI         1,535      62%             None         −4             None
  6      IND         1,444      50%             None         TEN         1,397      50%             None         −0             None
  6      LAC         1,494      51%             None         DEN         1,438      49%             None         0              None
  6      PIT         1,571      54%             None         LV          1,496      46%             None         1              None
  6      ATL         1,426      60%             None         CAR         1,309      40%             None         3              None
  6      DET         1,568      43%             None         DAL         1,565      57%             None         −2             None
  6      CIN         1,526      59%             None         NYG         1,411      41%             None         3              None
  6      BUF         1,663      67%             None         NYJ         1,487      33%             None         5              None
  7      DEN         1,438      25%             None         NO          1,580      75%             None         −8             None
  7      NE          1,402      35%             None         JAX         1,458      65%             None         −4             None
  7      SEA         1,531      58%             None         ATL         1,426      42%             None         2              None
  7      TEN         1,397      14%             None         BUF         1,663      86%             None         −13            None
  7      CIN         1,526      47%             None         CLE         1,497      53%             None         −1             None
  7      HOU         1,524      38%             None         GB          1,557      62%             None         −3             None
  7      MIA         1,524      54%             None         IND         1,444      46%             None         1              None
  7      DET         1,568      46%             None         MIN         1,547      54%             None         −1             None
  7      PHI         1,535      61%             None         NYG         1,411      39%             None         3              None
  7      LV          1,496      47%             None         LA          1,469      53%             None         −1             None
  7      CAR         1,309      33%             None         WAS         1,384      67%             None         −5             None
  7      KC          1,670      48%             None         SF          1,637      52%             None         −1             None
  7      NYJ         1,487      32%             None         PIT         1,571      68%             None         −5             None
  7      BAL         1,600      48%             None         TB          1,562      52%             None         −0             None
  7      LAC         1,494      50%             None         ARI         1,444      50%             None         0              None
  8      MIN         1,547      54%             None         LA          1,469      46%             None         1              None
  8      BAL         1,600      58%             None         CLE         1,497      42%             None         2              None
  8      TEN         1,397      22%             None         DET         1,568      78%             None         −9             None
  8      IND         1,444      32%             None         HOU         1,524      68%             None         −5             None
  8      GB          1,557      57%             None         JAX         1,458      43%             None         2              None
  8      ARI         1,444      32%             None         MIA         1,524      68%             None         −5             None
  8      NYJ         1,487      55%             None         NE          1,402      45%             None         1              None
  8      ATL         1,426      26%             None         TB          1,562      74%             None         −7             None
  8      CHI         1,466      55%             None         WAS         1,384      45%             None         1              None
  8      NO          1,580      55%             None         LAC         1,494      45%             None         1              None
  8      BUF         1,663      62%             None         SEA         1,531      38%             None         3              None
  8      PHI         1,535      44%             None         CIN         1,526      56%             None         −2             None
  8      CAR         1,309      26%             None         DEN         1,438      74%             None         −7             None
  8      KC          1,670      67%             None         LV          1,496      33%             None         5              None
  8      DAL         1,565      33%             None         SF          1,637      67%             None         −5             None
  8      NYG         1,411      23%             None         PIT         1,571      77%             None         −8             None
  9      HOU         1,524      48%             None         NYJ         1,487      52%             None         −1             None
  9      DAL         1,565      62%             None         ATL         1,426      38%             None         4              None
  9      DEN         1,438      23%             None         BAL         1,600      77%             None         −8             None
  9      MIA         1,524      25%             None         BUF         1,663      75%             None         −8             None
  9      NO          1,580      78%             None         CAR         1,309      22%             None         9              None
  9      LV          1,496      39%             None         CIN         1,526      61%             None         −3             None
  9      LAC         1,494      43%             None         CLE         1,497      57%             None         −2             None
  9      IND         1,444      29%             None         MIN         1,547      71%             None         −6             None
  9      WAS         1,384      39%             None         NYG         1,411      61%             None         −3             None
  9      NE          1,402      44%             None         TEN         1,397      56%             None         −2             None
  9      CHI         1,466      46%             None         ARI         1,444      54%             None         −1             None
  9      DET         1,568      44%             None         GB          1,557      56%             None         −2             None
  9      LA          1,469      34%             None         SEA         1,531      66%             None         −4             None
  9      JAX         1,458      33%             None         PHI         1,535      67%             None         −5             None
  9      TB          1,562      29%             None         KC          1,670      71%             None         −6             None
  10     CIN         1,526      33%             None         BAL         1,600      67%             None         −5             None
  10     NYG         1,411      57%             None         CAR         1,309      43%             None         2              None
  10     NE          1,402      34%             None         CHI         1,466      66%             None         −5             None
  10     BUF         1,663      73%             None         IND         1,444      27%             None         7              None
  10     MIN         1,547      56%             None         JAX         1,458      44%             None         2              None
  10     DEN         1,438      16%             None         KC          1,670      84%             None         −11            None
  10     ATL         1,426      24%             None         NO          1,580      76%             None         −8             None
  10     SF          1,637      54%             None         TB          1,562      46%             None         1              None
  10     PIT         1,571      69%             None         WAS         1,384      31%             None         5              None
  10     TEN         1,397      30%             None         LAC         1,494      70%             None         −6             None
  10     NYJ         1,487      49%             None         ARI         1,444      51%             None         −0             None
  10     PHI         1,535      39%             None         DAL         1,565      61%             None         −3             None
  10     DET         1,568      49%             None         HOU         1,524      51%             None         −0             None
  10     MIA         1,524      51%             None         LA          1,469      49%             None         0              None
  11     WAS         1,384      24%             None         PHI         1,535      76%             None         −8             None
  11     GB          1,557      56%             None         CHI         1,466      44%             None         2              None
  11     JAX         1,458      29%             None         DET         1,568      71%             None         −6             None
  11     LV          1,496      39%             None         MIA         1,524      61%             None         −3             None
  11     LA          1,469      52%             None         NE          1,402      48%             None         1              None
  11     CLE         1,497      32%             None         NO          1,580      68%             None         −5             None
  11     BAL         1,600      47%             None         PIT         1,571      53%             None         −1             None
  11     MIN         1,547      64%             None         TEN         1,397      36%             None         4              None
  11     ATL         1,426      41%             None         DEN         1,438      59%             None         −2             None
  11     SEA         1,531      29%             None         SF          1,637      71%             None         −6             None
  11     KC          1,670      44%             None         BUF         1,663      56%             None         −2             None
  11     CIN         1,526      47%             None         LAC         1,494      53%             None         −1             None
  11     IND         1,444      37%             None         NYJ         1,487      63%             None         −4             None
  11     HOU         1,524      37%             None         DAL         1,565      63%             None         −4             None
  12     PIT         1,571      53%             None         CLE         1,497      47%             None         1              None
  12     KC          1,670      86%             None         CAR         1,309      14%             None         12             None
  12     MIN         1,547      54%             None         CHI         1,466      46%             None         1              None
  12     TEN         1,397      27%             None         HOU         1,524      73%             None         −7             None
  12     DET         1,568      61%             None         IND         1,444      39%             None         3              None
  12     NE          1,402      27%             None         MIA         1,524      73%             None         −7             None
  12     TB          1,562      64%             None         NYG         1,411      36%             None         4              None
  12     DAL         1,565      68%             None         WAS         1,384      32%             None         5              None
  12     DEN         1,438      35%             None         LV          1,496      65%             None         −4             None
  12     SF          1,637      54%             None         GB          1,557      46%             None         1              None
  12     ARI         1,444      31%             None         SEA         1,531      69%             None         −5             None
  12     PHI         1,535      52%             None         LA          1,469      48%             None         1              None
  12     BAL         1,600      58%             None         LAC         1,494      42%             None         2              None
  13     CHI         1,466      29%             None         DET         1,568      71%             None         −6             None
  13     NYG         1,411      24%             None         DAL         1,565      76%             None         −8             None
  13     MIA         1,524      38%             None         GB          1,557      62%             None         −3             None
  13     LV          1,496      22%             None         KC          1,670      78%             None         −9             None
  13     LAC         1,494      53%             None         ATL         1,426      47%             None         1              None
  13     PIT         1,571      49%             None         CIN         1,526      51%             None         −0             None
  13     HOU         1,524      52%             None         JAX         1,458      48%             None         1              None
  13     ARI         1,444      29%             None         MIN         1,547      71%             None         −6             None
  13     IND         1,444      49%             None         NE          1,402      51%             None         −0             None
  13     SEA         1,531      49%             None         NYJ         1,487      51%             None         −0             None
  13     TEN         1,397      45%             None         WAS         1,384      55%             None         −1             None
  13     TB          1,562      76%             None         CAR         1,309      24%             None         8              None
  13     LA          1,469      28%             None         NO          1,580      72%             None         −6             None
  13     PHI         1,535      34%             None         BAL         1,600      66%             None         −5             None
  13     SF          1,637      39%             None         BUF         1,663      61%             None         −3             None
  13     CLE         1,497      51%             None         DEN         1,438      49%             None         0              None
  14     GB          1,557      41%             None         DET         1,568      59%             None         −2             None
  14     NYJ         1,487      38%             None         MIA         1,524      62%             None         −3             None
  14     ATL         1,426      27%             None         MIN         1,547      73%             None         −7             None
  14     NO          1,580      67%             None         NYG         1,411      33%             None         5              None
  14     CAR         1,309      17%             None         PHI         1,535      83%             None         −11            None
  14     CLE         1,497      33%             None         PIT         1,571      67%             None         −5             None
  14     LV          1,496      34%             None         TB          1,562      66%             None         −5             None
  14     JAX         1,458      52%             None         TEN         1,397      48%             None         0              None
  14     SEA         1,531      55%             None         ARI         1,444      45%             None         1              None
  14     BUF         1,663      70%             None         LA          1,469      30%             None         6              None
  14     CHI         1,466      22%             None         SF          1,637      78%             None         −9             None
  14     LAC         1,494      21%             None         KC          1,670      79%             None         −9             None
  14     CIN         1,526      37%             None         DAL         1,565      63%             None         −4             None
  15     LA          1,469      22%             None         SF          1,637      78%             None         −9             None
  15     DAL         1,565      77%             None         CAR         1,309      23%             None         8              None
  15     KC          1,670      67%             None         CLE         1,497      33%             None         5              None
  15     MIA         1,524      43%             None         HOU         1,524      57%             None         −2             None
  15     NYJ         1,487      47%             None         JAX         1,458      53%             None         −1             None
  15     WAS         1,384      20%             None         NO          1,580      80%             None         −10            None
  15     BAL         1,600      69%             None         NYG         1,411      31%             None         6              None
  15     CIN         1,526      61%             None         TEN         1,397      39%             None         3              None
  15     NE          1,402      37%             None         ARI         1,444      63%             None         −4             None
  15     IND         1,444      44%             None         DEN         1,438      56%             None         −2             None
  15     BUF         1,663      56%             None         DET         1,568      44%             None         2              None
  15     TB          1,562      53%             None         LAC         1,494      47%             None         1              None
  15     PIT         1,571      48%             None         PHI         1,535      52%             None         −1             None
  15     GB          1,557      47%             None         SEA         1,531      53%             None         −1             None
  15     CHI         1,466      32%             None         MIN         1,547      68%             None         −5             None
  15     ATL         1,426      33%             None         LV          1,496      67%             None         −5             None
  16     CLE         1,497      39%             None         CIN         1,526      61%             None         −3             None
  16     HOU         1,524      25%             None         KC          1,670      75%             None         −8             None
  16     PIT         1,571      39%             None         BAL         1,600      61%             None         −3             None
  16     NYG         1,411      41%             None         ATL         1,426      59%             None         −3             None
  16     NE          1,402      14%             None         BUF         1,663      86%             None         −12            None
  16     ARI         1,444      62%             None         CAR         1,309      38%             None         3              None
  16     DET         1,568      57%             None         CHI         1,466      43%             None         2              None
  16     TEN         1,397      36%             None         IND         1,444      64%             None         −4             None
  16     LA          1,469      40%             None         NYJ         1,487      60%             None         −3             None
  16     PHI         1,535      64%             None         WAS         1,384      36%             None         4              None
  16     DEN         1,438      35%             None         LAC         1,494      65%             None         −4             None
  16     MIN         1,547      45%             None         SEA         1,531      55%             None         −1             None
  16     JAX         1,458      38%             None         LV          1,496      62%             None         −4             None
  16     SF          1,637      59%             None         MIA         1,524      41%             None         2              None
  16     TB          1,562      42%             None         DAL         1,565      58%             None         −2             None
  16     NO          1,580      46%             None         GB          1,557      54%             None         −1             None
  17     KC          1,670      57%             None         PIT         1,571      43%             None         2              None
  17     BAL         1,600      54%             None         HOU         1,524      46%             None         1              None
  17     SEA         1,531      52%             None         CHI         1,466      48%             None         1              None
  17     NYJ         1,487      21%             None         BUF         1,663      79%             None         −9             None
  17     DEN         1,438      31%             None         CIN         1,526      69%             None         −6             None
  17     TEN         1,397      35%             None         JAX         1,458      65%             None         −4             None
  17     ARI         1,444      39%             None         LA          1,469      61%             None         −3             None
  17     GB          1,557      44%             None         MIN         1,547      56%             None         −2             None
  17     LAC         1,494      56%             None         NE          1,402      44%             None         2              None
  17     LV          1,496      32%             None         NO          1,580      68%             None         −5             None
  17     IND         1,444      48%             None         NYG         1,411      52%             None         −1             None
  17     CAR         1,309      15%             None         TB          1,562      85%             None         −12            None
  17     ATL         1,426      49%             None         WAS         1,384      51%             None         −0             None
  17     DAL         1,565      47%             None         PHI         1,535      53%             None         −1             None
  17     MIA         1,524      47%             None         CLE         1,497      53%             None         −1             None
  17     DET         1,568      34%             None         SF          1,637      66%             None         −5             None
  18     SF          1,637      69%             None         ARI         1,444      31%             None         6              None
  18     CAR         1,309      28%             None         ATL         1,426      72%             None         −7             None
  18     CLE         1,497      29%             None         BAL         1,600      71%             None         −6             None
  18     WAS         1,384      21%             None         DAL         1,565      79%             None         −9             None
  18     KC          1,670      74%             None         DEN         1,438      26%             None         7              None
  18     MIN         1,547      40%             None         DET         1,568      60%             None         −3             None
  18     CHI         1,466      31%             None         GB          1,557      69%             None         −6             None
  18     JAX         1,458      45%             None         IND         1,444      55%             None         −1             None
  18     SEA         1,531      52%             None         LA          1,469      48%             None         0              None
  18     LAC         1,494      43%             None         LV          1,496      57%             None         −2             None
  18     BUF         1,663      77%             None         NE          1,402      23%             None         8              None
  18     MIA         1,524      48%             None         NYJ         1,487      52%             None         −1             None
  18     NYG         1,411      27%             None         PHI         1,535      73%             None         −7             None
  18     CIN         1,526      37%             None         PIT         1,571      63%             None         −4             None
  18     NO          1,580      45%             None         TB          1,562      55%             None         −1             None
  18     HOU         1,524      61%             None         TEN         1,397      39%             None         3              None

</div>
        
:::
::::
