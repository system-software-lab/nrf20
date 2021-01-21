clear;

train3=load('train3.txt');

idx=kmeans(train3,4);

b=zeros([4 1000]);

i=0;
h=0;
current=0;
current_y=0;
temp=0;
count=2416;

result=zeros([2416 160]);

for i=1:2416
    current=idx(i);
    current_y=1;
    while b(current,current_y)~=0
        current_y=current_y+1;
    end
    b(current,current_y)=i;
end

while count~=0
    for h=1:4
        current_y=1;
        
        while b(h,current_y)~=0
            current_y=current_y+1;
        end
        
        if current_y==1 
            temp=b(h,current_y);
        else
            temp=b(h,current_y-1);
        end
        
        if temp==0
            continue;
        end
        result(2417-count,:)=train3(temp,:);

        count=count-1;
        if count==0
            break;
        end
        
        if current_y==1
            b(h,current_y)=0;
        else
            b(h,current_y-1)=0;
        end

    end
    
end

fid=fopen('train883.txt','wt');

for i= 1:2416
	fprintf(fid,'%3d,',result(i,:));
	fprintf(fid,'\n');
end

fclose(fid);
