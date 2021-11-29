<?php
// https://leetcode.com/problems/game-of-life/

// first version
function gameOfLife($board){
    $m = count($board); // number of rows
    $updated_board = $board;
    for($i = 0; $i < $m; $i++){
        $n = count($board[$i]); // number of columns
        $cur_row = $board[$i]; // current row
            
        // first row
        if($i == 0){
            for($j = 0; $j < $n; $j++){
                $cur_cell = $cur_row[$j];
                $next_row = $board[$i+1]; // next row

                // first column
                if($j == 0){
                    $same_row_cells = [$cur_row[$j+1]];
                    $next_row_cells = [$next_row[$j], $next_row[$j+1]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";

                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                // last column
                elseif($j == $n-1){
                    $same_row_cells = [$cur_row[$j-1]];
                    $next_row_cells = [$next_row[$j-1], $next_row[$j]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                else{
                    $same_row_cells = [$cur_row[$j-1], $cur_row[$j+1]];
                    $next_row_cells = [$next_row[$j-1], $next_row[$j], $next_row[$j+1]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
            }
        }
        // last row
        elseif($i == $m-1){
            for($j = 0; $j < $n; $j++){
                $cur_cell = $cur_row[$j];
                $prev_row = $board[$i-1]; // previous row

                // first column
                if($j == 0){
                    $prev_row_cells = [$prev_row[$j], $prev_row[$j+1]];
                    $same_row_cells = [$cur_row[$j+1]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($prev_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                // last column
                elseif($j == $n-1){
                    $prev_row_cells = [$prev_row[$j-1], $prev_row[$j]];
                    $same_row_cells = [$cur_row[$j-1]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($prev_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                else{
                    $prev_row_cells = [$prev_row[$j-1], $prev_row[$j], $prev_row[$j+1]];
                    $same_row_cells = [$cur_row[$j-1], $cur_row[$j+1]];
                    $live_neighbours = array_sum($same_row_cells) + array_sum($prev_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
            }
        }
        else{
            for($j = 0; $j < $n; $j++){
                $cur_cell = $cur_row[$j];
                $prev_row = $board[$i-1]; // previous row
                $next_row = $board[$i+1]; // next row

                // first column
                if($j == 0){
                    $prev_row_cells = [$prev_row[$j], $prev_row[$j+1]];
                    $same_row_cells = [$cur_row[$j+1]];
                    $next_row_cells = [$next_row[$j], $next_row[$j+1]];
                    $live_neighbours = array_sum($prev_row_cells) + array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                // last column
                elseif($j == $n-1){
                    $prev_row_cells = [$prev_row[$j-1], $prev_row[$j]];
                    $same_row_cells = [$cur_row[$j-1]];
                    $next_row_cells = [$next_row[$j-1], $next_row[$j]];
                    $live_neighbours = array_sum($prev_row_cells) + array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
                else{
                    $prev_row_cells = [$prev_row[$j-1], $prev_row[$j], $prev_row[$j+1]];
                    $same_row_cells = [$cur_row[$j-1], $cur_row[$j+1]];
                    $next_row_cells = [$next_row[$j-1], $next_row[$j], $next_row[$j+1]];
                    $live_neighbours = array_sum($prev_row_cells) + array_sum($same_row_cells) + array_sum($next_row_cells);
                    echo "$i - $j : $live_neighbours<br>";
                    
                    // current cell is dead (0)
                    if($cur_cell == 0){
                        if($live_neighbours == 3){
                            $updated_board[$i][$j] = 1;
                        }
                    }
                    // current cell is live (1)
                    else{
                        // underpopulation
                        if($live_neighbours < 2){
                            $updated_board[$i][$j] = 0;
                        }
                        // overpopulation
                        elseif($live_neighbours > 3){
                            $updated_board[$i][$j] = 0;
                        }
                    }
                }
            }
        }
    }
    echo "<br>";
    foreach($updated_board as $rows){
        foreach($rows as $cell){
            echo "$cell ";
        }
        echo "<br>";
    }
    var_dump($updated_board);
    return $updated_board;
}

$board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]; // output should be [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
$board1 = [[1,1],[1,0]]; // output should be [[1,1],[1,1]]
$board2 = [[0,1,0],[1,1,1],[0,1,0]];

gameOfLife($board);
gameOfLife($board1);
gameOfLife($board2);
$board3 = gameOfLife($board2);
gameOfLife($board3);

?>