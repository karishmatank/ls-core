"""
**** Problem description (provided) ****
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what 
determines a valid structure:
    - The building blocks are cubes.
    - The structure is built in layers.
    - The top layer is a single block.
    - A block in an upper layer must be supported by four blocks in a lower layer.
    - A block in a lower layer can support more than one block in an upper layer.
    - You cannot leave gaps between blocks.

Write a program that, given the number of available blocks, calculates the number of blocks left over after building 
the tallest possible valid structure.

**** Step 1: Understand the problem ****

Input: Integer representing the number of available blocks
Output: Integer representing blocks left over
Problem requirements:
    - Explicit:
        - Units are in cubes
        - Top most layer is only one cube
        - Each block in a layer touches 4 blocks in the layer below
        - Each block in a lower layer can support more than one block in an upper layer
        - No gaps between blocks when supporting
        - We are given the number of available blocks and must return an integer of the blocks *left over*
          after building the tallest possible structure
    - Implicit:
        - See "Visual sequence" below

Visual sequence:
    - Top layer is just one block
    - Bottom layer is 4 blocks, as 4 blocks must support the one above (2 ** 2)
    - Layer under that would be 9 blocks, which all work together to support the 4 above (3 ** 2)
    - So this essentially looks like a block pyramid, where the number of blocks in a layer has a direct relationship
      with the layer #
        - So if we assume layer 1 is the top layer, layer 1 = 1 block, then layer 2 = 2 ** 2 = 4 blocks, etc.

Questions:
    - How should the program react if we get 0 blocks or a negative integer from the user?
    - (Missed, taken from discussion) Is a lower layer valid if it has more blocks than it needs?
    - (Missed, taken from discussion) Will there always be left-over blocks?

**** Step 2: Examples and test cases ****
Using the test cases below, refining our understanding of the problem:
    - If we get an input of 0, we should return 0 as there are no blocks to build a pyramid and thus no blocks left over
    - Still not sure about treating a negative integer
    - This confirms my understanding based off of the block pyramid structure I was envisioning
        - If we have one block, we use that to build layer 1 (top), which leaves no blocks
        - If we have 2 blocks, we use one for layer 1, and 1 is left behind
        - If we have 4 blocks, we only have room for layer 1, so 3 are left behind
        - If we have 5 blocks, we can build both layer 1 (1 block) and layer 2 (2 ** 2 = 4 blocks), which means we
          use all 5
        - If we have 6 blocks, we use 5 as mentioned prior and have 1 left over
        - If we have 14 blocks, we can build layer 1 (1 block), layer 2 (4 blocks), layer 3 (9 blocks) = 14 blocks
          and thus have 0 left over

**** Step 3: Data structures ****
Not immediately clear. Doesn't jump out to me that a specific structure would be useful, but maybe we use a list
to denote the # of blocks that we've allocated to use for a specific layer. Seems however that we can just use
a variable and increment that up as we go forward.

**** Step 4: Algorithm ****
1. Assign a variable 'blocks_used' to the value 0. This will represent the # of blocks used along the way in total
   across layers. We also start off with the input, which represents blocks available
2. Assign a variable 'layer_num' to the value 1
3. Calculate the number of blocks necessary to build the next layer
    a. The next layer is defined as the layer number assigned to the layer_num variable
4. If blocks necessary to build next layer <= blocks available:
    a. Build that layer- Reflect blocks used by decrementing blocks available and incrementing blocks used, both by
       the number of blocks necessary to build that layer
    b. Increment layer_num to reflect the next layer we would build by adding 1
    c. Go back to step 3
5. If blocks necessary > blocks available, we can't build the next layer, so we should stop checking
6. Return blocks available, which is now just the blocks left over

How to determine the number of blocks necessary to build the next layer (step 3)?
- Input: Integer (layer number)
- Output: Output (Number of blocks needed)
- Requirements:
    - We take the layer number, which represents the next layer we will build underneath existing blocks, and
      calculate the number of blocks necessary to build the layer by taking the square of that number
- Algorithm:
    - Get input (layer number)
    - Return square of layer input, which is the number of blocks needed

**** Step 5: Code ****
See below

"""

def calculate_leftover_blocks(blocks_available):
    layer_number = 1

    while True:
        blocks_needed = calculate_blocks_needed(layer_number)
        if blocks_needed <= blocks_available:
            blocks_available -= blocks_needed
            layer_number += 1
        else:
            break
    
    return blocks_available


def calculate_blocks_needed(layer_number):
    return layer_number ** 2




# Test cases
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
