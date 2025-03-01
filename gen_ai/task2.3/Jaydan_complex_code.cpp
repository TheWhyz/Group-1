// Old code
double getObjectsWeight(binTreeNode * r)
{
    double invalid = -1.0;
    double combinedWeight = 0;
    double leftWeight;
    double rightWeight;
    int armWeight;

    //If both the left and right side are NULL
    //then it is a leaf function, grab the weight of the node
    if(r->getLeft() == NULL && r->getRight() == NULL)
    {
        return r->getWeight();
    }
    
    //Get the left weight node
    leftWeight = getObjectsWeight(r->getLeft());

    //If the node returns invalid then entire tree is invalid
    if(leftWeight == invalid)
        return invalid;

    //Add the leftWeight to combinedWeight
    combinedWeight += leftWeight;

    //Set the armWeight to the left arm weight and multiply
    //leftWeight and armWeight
    armWeight = r->getLeft()->getArmLength();
    leftWeight *= armWeight;

    //Do the same for the right side
    rightWeight = getObjectsWeight(r->getRight());
    if(rightWeight == invalid)
        return invalid;
    combinedWeight += rightWeight;
    armWeight = r->getRight()->getArmLength();
    rightWeight *= armWeight;

    //if the leftWeight and rightWeight are equal
    //then return the weight otherwise return invalid
    if(leftWeight == rightWeight) 
        return combinedWeight;
    else
        return invalid;
    

}


// New code 
double getObjectsWeight(binTreeNode* node) {
    constexpr double INVALID_WEIGHT = -1.0;

    // Base case: If the node is a leaf, return its weight
    if (!node->getLeft() && !node->getRight()) {
        return node->getWeight();
    }

    // Recursively calculate the left and right subtree weights
    double leftWeight = (node->getLeft()) ? getObjectsWeight(node->getLeft()) : 0;
    double rightWeight = (node->getRight()) ? getObjectsWeight(node->getRight()) : 0;

    // If either side is invalid, return invalid
    if (leftWeight == INVALID_WEIGHT || rightWeight == INVALID_WEIGHT) {
        return INVALID_WEIGHT;
    }

    // Compute the torque for both sides
    double leftTorque = leftWeight * node->getLeft()->getArmLength();
    double rightTorque = rightWeight * node->getRight()->getArmLength();

    // Check if the torques are balanced
    if (leftTorque != rightTorque) {
        return INVALID_WEIGHT;
    }

    // Return the total weight of the subtree
    return leftWeight + rightWeight;
}
